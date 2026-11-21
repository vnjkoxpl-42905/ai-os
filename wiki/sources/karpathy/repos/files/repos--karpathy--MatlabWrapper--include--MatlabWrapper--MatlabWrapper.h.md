---
type: source
subject: "GitHub source repos/karpathy/MatlabWrapper/include/MatlabWrapper/MatlabWrapper.h"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/MatlabWrapper/include/MatlabWrapper/MatlabWrapper.h]
semantic-status: complete-named-text-read
---

# repos/karpathy/MatlabWrapper/include/MatlabWrapper/MatlabWrapper.h

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/MatlabWrapper/include/MatlabWrapper/MatlabWrapper.h), SHA-256 `2979e8b20b2502ae3fb527939de4563a64bfeec06a74d4fd41b340675aa8db29`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt:

```text
/* MatlabWrapper Andrej Karpathy August 27, 2012 BSD Licence */ #ifndef MATLAB_WRAPPER_H__ #define MATLAB_WRAPPER_H__ #include
```

MatlabWrapper header implementation and interactive example fully read, credited Karpathy August2012 BSD. Minimal Eigen float matrix bridge lazily starts MATLAB engine, transfers numeric copies, receives2D single/double with explicit cast, executes commands and interactive qq exit, and visualizes then retrieves random matrix. Ownership cleanup explicit for mxArray copies. Historical limits: constructor leaves engine pointer uninitialized but destructor closes it, lazy init failure not checked, receive/exec/interact assume init, old dimension-pointer API, no automated equality assertion in test. Convenience visualization workflow, no current dependency installation or execution.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
/*
MatlabWrapper

Andrej Karpathy
August 27, 2012
BSD Licence
*/

#ifndef MATLAB_WRAPPER_H__
#define MATLAB_WRAPPER_H__

#include <iostream>
#include <string>
#include <map>
#include <Eigen/Eigen>
#include "engine.h"

#define MATLAB_BUF_SIZE 1024

using namespace std;

/*
Lets you use Matlab from C++ effortlessly
Example usage:

Eigen::MatrixXf X = Eigen::MatrixXf::Random(3,4);
cout << X << endl;

// create wrapper and visualize tiny 3x4 random matrix
MatlabWrapper mw;
mw.sendMat("X", X);
mw.exec("imshow(X, [])", true); //true indicates that we want matlab to pause for keypress

// enter interactive session! Enter 'qq' to return 
mw.interact();

// receive matrix X back and print it to make sure it's the same
Eigen::MatrixXf mat;
mw.receiveMat("X", mat);
cout << mat << endl;
*/

class MatlabWrapper {
  
  public:
    MatlabWrapper();
    ~MatlabWrapper();
    
    // start the engine. Returns false on error.
    bool init(); 
    
    // send a matrix to matlab engine
    void sendMat(const string name, const Eigen::MatrixXf &mat);  
    
    // receive a matrix back from matlab engine
    void receiveMat(const string name, Eigen::MatrixXf &mat) const;  
    
    // execute a command in matlab
    void exec(const string cmd, const bool waitForKey = false) const;
    
    // starts interactive mode where you can type anything and get response back from MATLAB  
    // enter qq to exit interactive mode
    void interact(); 
    
    bool verbose_;
    
  protected:
    
    Engine *ep_;
    bool initted_;
    char buffer_[MATLAB_BUF_SIZE]; // output buffer for matlab to talk back to us
};

#endif

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
