"""Pre-generate item lists, timing schedules and participant groups.

Everything is fixed with a seed, so the same files come out every time. The
robot trial node reads these CSV files; nothing is randomised during a session.

Timing per item (seconds):
    move in (MOVE) -> screen on for `view` -> screen off, move out (MOVE) -> wait `wait`

Coordinated:   view 2.0, wait 1.0 for every item (one item every 5 s).
Uncoordinated: view from 1.0 to 3.0 and wait from 0.0 to 2.0, each value used
               equally often, so the means (2.0 and 1.0) and the trial length
               are exactly the same as in the coordinated condition.

Usage:
    python tools/make_schedules.py [out_dir]     (default: schedules/)
"""
import csv
import random
import sys
from pathlib import Path

SEED = 2026
MOVE = 1.0  # nominal move time; update after timing the real arm (week 2)
N_ITEMS = 20
N_PRACTICE = 10
COLOURS = ["RED", "BLUE", "GREEN", "YELLOW"]
NUMBERS = list(range(1, 10)) * 2 + [3, 7]  # 20 numbers, same set in both lists
VIEWS = [1.0, 1.5, 2.0, 2.5, 3.0]
WAITS = [0.0, 0.5, 1.0, 1.5, 2.0]
N_PARTICIPANTS = 18  # 16 complete plus spares

rng = random.Random(SEED)


def item_list(n, numbers):
    """Colours balanced, no repeated item, colour or number back to back."""
    colours = (COLOURS * n)[:n]
    while True:
        c = colours[:]
        k = numbers[:]
        rng.shuffle(c)
        rng.shuffle(k)
        if all(c[i] != c[i - 1] and k[i] != k[i - 1] for i in range(1, n)):
            return list(zip(c, k))


def uncoordinated_timing(n):
    """Shuffle views and waits until the sequence meets the checks below."""
    views = VIEWS * (n // len(VIEWS))
    waits = WAITS * (n // len(WAITS))
    while True:
        v = views[:]
        w = waits[:]
        rng.shuffle(v)
        rng.shuffle(w)
        tight = sum(1 for a, b in zip(v, w) if a <= 1.5 and b <= 0.5)
        no_double_short = all(not (v[i] == 1.0 and v[i - 1] == 1.0) for i in range(1, n))
        # last wait 1.0 keeps the trial exactly as long as the coordinated one
        full_range = (1.0, 0.0) in zip(v, w) and (3.0, 2.0) in zip(v, w)  # gaps 3 to 7 s
        if v[0] >= 2.0 and w[-1] == 1.0 and tight >= 4 and no_double_short and full_range:
            return list(zip(v, w))


def practice_timing():
    """First half regular, second half varied, so practice favours neither condition."""
    half = N_PRACTICE // 2
    varied = [(1.0, 0.0), (3.0, 2.0), (1.5, 0.5), (2.5, 1.5), (2.0, 1.0)]
    rng.shuffle(varied)
    return [(2.0, 1.0)] * half + varied


def write_items(path, items):
    with open(path, "w", newline="") as f:
        out = csv.writer(f)
        out.writerow(["index", "colour", "number"])
        for i, (c, k) in enumerate(items, 1):
            out.writerow([i, c, k])


def write_timing(path, timing):
    with open(path, "w", newline="") as f:
        out = csv.writer(f)
        out.writerow(["index", "view_s", "wait_s", "onset_s", "onset_to_next_s"])
        t = MOVE
        for i, (v, w) in enumerate(timing, 1):
            gap = v + MOVE + w + MOVE
            out.writerow([i, v, w, round(t, 2), gap if i < len(timing) else ""])
            t += gap


def main(out_dir):
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)

    list_a = item_list(N_ITEMS, NUMBERS)
    list_b = item_list(N_ITEMS, NUMBERS)
    practice = item_list(N_PRACTICE, rng.sample(range(1, 10), 9) + [5])
    coord = [(2.0, 1.0)] * N_ITEMS
    uncoord = uncoordinated_timing(N_ITEMS)

    write_items(out / "items_A.csv", list_a)
    write_items(out / "items_B.csv", list_b)
    write_items(out / "items_practice.csv", practice)
    write_timing(out / "timing_coordinated.csv", coord)
    write_timing(out / "timing_uncoordinated.csv", uncoord)
    write_timing(out / "timing_practice.csv", practice_timing())

    # 4 groups: order (coordinated first or second) x list paired with coordinated
    groups = [("C-U", "A"), ("C-U", "B"), ("U-C", "A"), ("U-C", "B")]
    slots = (groups * (N_PARTICIPANTS // 4 + 1))[:N_PARTICIPANTS]
    first16, spares = slots[:16], slots[16:]
    rng.shuffle(first16)
    with open(out / "participants.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["participant", "group", "order", "trial1", "list1", "trial2", "list2"])
        for i, (order, coord_list) in enumerate(first16 + spares, 1):
            unc_list = "B" if coord_list == "A" else "A"
            conds = ["coordinated", "uncoordinated"] if order == "C-U" else ["uncoordinated", "coordinated"]
            lists = [coord_list if c == "coordinated" else unc_list for c in conds]
            w.writerow([f"P{i:02d}", groups.index((order, coord_list)) + 1, order,
                        conds[0], lists[0], conds[1], lists[1]])

    for name, timing in [("coordinated", coord), ("uncoordinated", uncoord)]:
        gaps = [v + w + 2 * MOVE for v, w in timing]
        print(f"{name:>13}: mean view {sum(v for v, _ in timing) / N_ITEMS:.2f} s, "
              f"mean gap {sum(gaps) / N_ITEMS:.2f} s, gaps {min(gaps)} to {max(gaps)} s, "
              f"trial {sum(gaps[:-1]) + timing[-1][0] + 2 * MOVE:.1f} s")
    print(f"Wrote schedules to {out}/")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "schedules")
