# Uses python3
"""
** Problem **
    Find fewest points covering all the segments.

What is a greedy move and why is it a safe move?
** Greedy move **
    Starting from the segment with minimum right endpoint, the greedy move
    should be making the right endpoint of this segment as the 1st point.
* Why safe move?
    1. Assuming an optimal solution A differentiating in the 'first move' from
       the greedy solution G, i.e., Coordinate of point A_1 is smaller than the
       minimum right point G_1.
    2. Moving A_1 to right until reaching G_1 is no worse than the original
       solution A b/c it won't lose any already covered segment.
    3. By induction, at every step a greedy move G_i is no worse than A_i, and
       hence, it is a SAFE MOVE.
"""
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def optimal_points(segments):
    # Sort segments by the right endpoint
    sorted_segments = sorted(segments, key=lambda x: x.end)
    points = []
    while len(sorted_segments) > 0:
        s0 = sorted_segments[0]
        points.append(s0.end)
        for s in sorted_segments[1:]:
            if s.start <= s0.end:
                sorted_segments.remove(s)  # segment covered
        sorted_segments.remove(s0)
    return points


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
