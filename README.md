## Introduction

Enapter Dryer is a hybrid temperature/pressure swing adsorption system increasing hydrogen purity to 99,999%. Find out more about [Enapter Dryer](https://go.enapter.com/aT7yS).

We developed [Dryer Control Network](https://go.enapter.com/2cHU1) - technology that allows you to control and monitor Enapter Dryer from [Electrolyser](https://go.enapter.com/UUBKr) Web GUI or Modbus TCP interfaces. Also when Dryer Control Network is enabled, Dryer starts automatically when at least one of connected electrolysers is steady.

## Requirements

This repository contains various examples of Dryer Control Network usage. All examples are written in python3 language. Before using examples make sure that the following are installed on your system:

- [python3](https://wiki.python.org/moin/BeginnersGuide/Download)
- [pip](https://pip.pypa.io/en/stable/installing/)

After that make sure all required python packages are installed. You can install them system-wide as:

```bash
python3 -m pip install requirements.txt
```

or by using [virtualenv](https://docs.python.org/3/library/venv.html).

### Examples

:warning: Before using any example make sure to go through list below

* Dryer must be connected to the same pipeline as electrolysers.
* DCN/IDCN should be enabled via Enapter Mobile App or manually. For more info see [Dryer Control Network Quick Start Guide](https://go.enapter.com/jvXwD).

Each example contains an explanation README.md file and a python script. While operating Dryer can be in various [logic states](https://go.enapter.com/p2Q9o).
