# coding: UTF-8
"""
"""

batchSize = 16
learningRateBase = 0.001
learningRateDecreaseStep = 100
epochNum = 100                    # train epoch
generateNum = 3                   # number of generated poems per time

trainPoems = "dataset/poetry.txt" # training file location
checkpointsPath = "./checkpoints" # checkpoints location