# src/main.py
import argparse
import os
import tensorflow as tf
import numpy
import pandas as pd
import sklearn
import matplotlib.pyplot as plt

def main(args):
    print(f"Mode: {args.mode}")
    print(f"Data dir: {args.data_dir}")
    print(f"TensorFlow version: {tf.__version__}")
    print(f"Numpy version: {numpy.__version__}")
    print(f"Pandas version: {pd.__version__}")
    print(f"Scikit-learn version: {sklearn.__version__}")


    if args.mode == "train":
        # Itt hívd meg a train loop-ot, dataloader-t stb.
        print("Training start (placeholder)...")
    elif args.mode == "eval":
        print("Evaluation (placeholder)...")
    else:
        print("Unknown mode")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", type=str, default="train", choices=["train","eval","serve"])
    parser.add_argument("--data-dir", type=str, default="/data")
    args = parser.parse_args()
    main(args)
