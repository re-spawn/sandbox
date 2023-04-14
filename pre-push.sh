#!/bin/bash

# [ "$LK_GIT_PRE_PUSH" = 0 ] && exit 0
set -e
python test_that_fails.py
python test_that_passes.py