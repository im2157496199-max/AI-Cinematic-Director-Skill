#!/usr/bin/env python3
import math

def snap_length(duration_s: float, fps: float, step: int, base: int = 1, min_length: int = 1):
    if duration_s <= 0 or fps <= 0:
        raise ValueError("duration_s and fps must be > 0")
    target=round(duration_s*fps)
    n=round((target-base)/step)
    n=max(0,n)
    length=base+n*step
    while length < min_length:
        n+=1
        length=base+n*step
    actual=length/fps
    return {
        "target_frames_raw": target,
        "adapter_length": length,
        "actual_duration_s": actual,
        "duration_delta_s": actual-duration_s,
    }

if __name__ == "__main__":
    import argparse, json
    p=argparse.ArgumentParser()
    p.add_argument("duration_s", type=float)
    p.add_argument("fps", type=float)
    p.add_argument("--step", type=int, required=True)
    p.add_argument("--base", type=int, default=1)
    p.add_argument("--min-length", type=int, default=1)
    a=p.parse_args()
    print(json.dumps(snap_length(a.duration_s,a.fps,a.step,a.base,a.min_length),indent=2))
