---
type: source
subject: "GitHub source repos/karpathy/MatlabWrapper/Readme.md"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/MatlabWrapper/Readme.md]
semantic-status: complete-named-text-read
---

# repos/karpathy/MatlabWrapper/Readme.md

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/MatlabWrapper/Readme.md), SHA-256 `0468e2cdb4bc82528fe0f7da476c5894853cb30dbedaa4be35da9ec31a95d03c`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt:

```text
# MatlabWrapper Andrej Karpathy 27 August 2012 This C++ library is a convenience wrapper around
```

Llm.c script documentation preserves comparable effective batch sizes across GPU counts while trading recomputation and microbatch size against memory and runtime; the reference scripts explicitly omit checkpoints, Hellaswag and resume. MatlabWrapper favors reuse and an interactive debugging bridge instead of reimplementing k-means, and first asks users to establish the official engine demo before wrapper-specific diagnosis. MinGPT project readmes label addition and character modeling examples, with text8/enwik8 still TODO. Nanochat covers tokenization through chat inference, uses a depth dial for principled scaling, measures bits per byte against steps/time/FLOPs together with CORE and throughput, and requires candidate changes to work across depths. It acknowledges unexercised device paths, CPU capability limits, explicit dtype choices, incomplete fp16 RL support, and AI-contribution disclosure when authors do not fully understand code. Captured price/leaderboard/hardware claims are dated results, not reruns. NanoGPT dataset readmes report token/split counts and provenance without turning training data into Karpathy beliefs; neuraltalk folder readmes separate data and checkpoints from code.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

````text
# MatlabWrapper
Andrej Karpathy
27 August 2012

This C++ library is a convenience wrapper around Matlab Engine, especially 
if you use Eigen matrix library for working with matrices. It should be quite 
easy to adapt it to other library types as well.

## Usage

Consider the simplest example: You have an ```Eigen::MatrixXf X;``` lying around
and you'd love to run k-means on its rows. But naturally, you don't feel like 
re-implementing k-means for Eigen matrices from scratch! So you write:
```c++
  
  MatlabWrapper mw;
  mw.sendMat("X", X); // transfer it over to the engine under name "X"
  mw.exec("[IDX, C] = kmeans(X, 10);");
  Eigen::MatrixXf mat;
  mw.receiveMat("C", mat);
  
  // done!
```

That felt good. Now supose you've computing something complicated and would
really like to explore it a bit interactively-- do a few plots, run some statistics,
etc. No problem:

```c++
  MatlabWrapper mw;
  mw.sendMat("X", X);
  mw.interact();
```

This will start an interactive session with matlab right in your shell! You get
to type whatever you wish:
```Matlab
>> plot(X(:,1), X(:,2)); // interesting!
>> close;
>> hist(X); 
>> close;
```

Entering qq will resume the c++ program right where it left off. This is quite
great for debugging as well.

## Install
Eigen library is a dependency, and so is Matlab, naturally.
If you don't have eigen, install it with 
```
$ sudo apt-get install libeigen3-dev
```

Also make sure you have tcsh, which is require for matlab engine to work
```
sudo apt-get install tcsh
```
At this point you may want to get the official MATLAB demo to run (see below)

then to install this library.
```
$ git clone git@github.com:karpathy/MatlabWrapper.git 
$ cd MatlabWrapper
$ mkdir build 
$ cd build
$ cmake ..
$ make
$ ./test1
```

where last line runs a small demo. Naturally, the above will probably not run
right away because these things never do. Have a look inside CMakeLists.txt 
and modify the include/library paths according to your system preferences. I
tried to document it as best I could.

## Getting Matlab Engine to run

If you haven't used Matlab Engine yet, try to get their demo running first.
Here is the main documentation:
http://www.mathworks.com/help/techdoc/matlab_external/f29148.html

In particular of interest is this link on getting their engdemo.c running:
http://www.mathworks.com/help/techdoc/matlab_external/bsq776w-1.html#bsq78dr-9

If you can get that running, you're halfway there! Problems I ran across:
- You must have tcsh installed! ```sudo apt-get install tcsh```
- I needed to add a missing .so file to my $LD_LIBRARY_PATH in .bashrc and source it.
- They were looking for libc.so.6 in /lib64/ but mine was in /lib/x86_64-linux-gnu/
so I had to symlink it over.

Good luck!

## License
BSD

````

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
