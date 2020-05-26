# copr-cherrytree

A Fedora repository for the [Cherrytree heiarchical note taking application](http://www.giuspen.com/cherrytree/).

This repository contains the spec files etc for building the [cherrytree COPR](https://copr.fedorainfracloud.org/coprs/bcotton/cherrytree/) I maintain. This content is licensed under the GNU GPLv3 (see [LICENSE](LICENSE) in this repository).

## Installation

### Fedora 31

Fedora 31 has **cherrytree** (the released Python2 application).

To install:

1. `sudo dnf copr enable bcotton/cherrytree`
2. `sudo dnf install cherrytree` 

Old builds of **cherrytree-future** are available, but due to new dependencies, it is no longer possible to build that package on Fedora 31 without adopting additional dependencies.

## Fedora 32 and Rawhide

Fedora 32 and Rawhide only provide the **cherrytree-future** package.
This is due to the difficulties in adding the necessary dependencies after the removal of Python2.
See my [blog post](https://funnelfiasco.com/blog/2020/04/30/cherrytree-updates-in-copr/) for more information.

To install:

1. `sudo dnf copr enable bcotton/cherrytree`
2. `sudo dnf install cherrytree-future`

### Upgrading from Fedora 31

I intentionally did not have the **cherrytree-future** package obsolete the **cherrytree** package. 
Because the "future" build is a pre-release, I want users to make an explicit decision to use it.
If you want to upgrade from Fedora 31 to Fedora 32 or Rawhide, you will first need to remove the **cherrytree** package and install **cherrytree-future**.

## Getting help

If you encounter problems with the package itself (e.g. dependency errors or missing files), please [file an issue](https://github.com/funnelfiasco/copr-cherrytree/issues) in this repo. You can also discuss it on [Fedora Discussion](https://discussion.fedoraproject.org/t/bcotton-cherrytree/10617).

If you encounter problems with the application, please report it [upstream](https://github.com/giuspen/cherrytree/issues).
