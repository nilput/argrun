#!/bin/bash
pydocmd build
cat build/pydocmd/index.md build/pydocmd/docs.md  > ../README.md
cd .. && m2r --overwrite README.md
