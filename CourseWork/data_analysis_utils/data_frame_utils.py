import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


def get_positions_list(frame):
    return frame['position'].dropna().unique()


def get_programing_languages(frame):
    return frame['language'].dropna().unique()