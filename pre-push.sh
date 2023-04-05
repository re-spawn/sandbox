#!/bin/bash
[[ $LK_GIT_PRE_PUSH -eq 0 ]] && exit 0
set -e
python test_example_passes.py
python test_example_fails.py