---
type: source
subject: "GitHub source repos/karpathy/MatlabWrapper/src/MatlabWrapper.cpp"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/MatlabWrapper/src/MatlabWrapper.cpp]
semantic-status: complete-named-text-read
---

# repos/karpathy/MatlabWrapper/src/MatlabWrapper.cpp

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/MatlabWrapper/src/MatlabWrapper.cpp), SHA-256 `d4365df838949c5baf765e12a799651c3ff2fa87d12fd5476072e4b4eabc5f44`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt:

```text
/* MatlabWrapper Andrej Karpathy August 27, 2012 BSD Licence */ #include <MatlabWrapper/MatlabWrapper.h> #include <stdio.h> using
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

#include <MatlabWrapper/MatlabWrapper.h>
#include <stdio.h>

using namespace std;

MatlabWrapper::MatlabWrapper() {
  initted_ = false; 
  verbose_ = true;
}

MatlabWrapper::~MatlabWrapper() {
  engClose(ep_); // close down the engine
}

bool MatlabWrapper::init() {
  
  if (!(ep_ = engOpen(""))) {
		fprintf(stderr, "\nCan't start MATLAB engine.\n");
		return false;
	}
	
	// connect Matlab engine to a char buffer for output
	buffer_[MATLAB_BUF_SIZE - 1] = '\0';
	engOutputBuffer(ep_, buffer_, MATLAB_BUF_SIZE - 1);
	
	initted_ = true;
	return true;
}

void MatlabWrapper::sendMat(const string name, const Eigen::MatrixXf &mat) {
  
  int N = mat.rows();
  int D = mat.cols();
  if(N <= 0 || D <= 0) {
    fprintf(stderr, "\nWow, weird matrix is of size %dx%d. Ignoring sendMat request.\n", N, D);
    return;
  }
  if(!initted_) { init(); }
  
  mxArray *X = mxCreateNumericMatrix(N, D, mxSINGLE_CLASS, mxREAL);
  memcpy((float *)mxGetData(X), mat.data(), sizeof(float)*N*D);
	engPutVariable(ep_, name.c_str(), X);
	mxDestroyArray(X); // the engine takes ownership of a copy
}

void MatlabWrapper::receiveMat(const string name, Eigen::MatrixXf &mat) const {
  
  mxArray *result = NULL;
  if ((result = engGetVariable(ep_, name.c_str())) == NULL) {
    printf("Variable %s is not defined! Ignoring request.\n", name.c_str());
    return;
  }
  
  int number_of_dims; 
  number_of_dims = mxGetNumberOfDimensions(result);
  if(number_of_dims != 2) {
    printf("Can only receive 2D matrix back! Exitting.\n");
    mxDestroyArray(result);
    return;
  }
  
  const int *dim_array = mxGetDimensions(result);
  int N= dim_array[0];
  int D= dim_array[1];
  
  mxClassID classType= mxGetClassID(result);
  if(classType == mxSINGLE_CLASS) { 
    mat.resize(N, D);
    memcpy(mat.data(), (float *)mxGetData(result), sizeof(float)*N*D);
    
  } else if(classType == mxDOUBLE_CLASS) {
    if(verbose_) printf("Oi! Variable %s is double, converting to single!\n", name.c_str());
    Eigen::MatrixXd proxy(N, D);
    memcpy(proxy.data(), (double *)mxGetData(result), sizeof(double)*N*D);
    mat = proxy.cast<float>();
    
  } else {
    printf("Error! Variable %s is not single/double. Ignoring.\n", name.c_str());
  }
  
  mxDestroyArray(result); // we own this newly allocated mxArray. Destroy it
}

void MatlabWrapper::exec(const string cmd, const bool waitForKey) const {

  engEvalString(ep_, cmd.c_str());
  if(waitForKey) {
    printf("Hit return to continue\n"); 
    fgetc(stdin);
  }
}

void MatlabWrapper::interact() {
  
  printf("Started interactive MATLAB session! Enter 'qq' to exit.\n");
  char str[MATLAB_BUF_SIZE + 1];
  while(true) {
    
    printf(">> ");
    fgets(str, MATLAB_BUF_SIZE, stdin);
    if(strcmp(str, "qq\n") == 0) break;
    
    engEvalString(ep_, str);
    printf("%s\n", buffer_);
  }
}




```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
