---
type: source
subject: "GitHub source repos/karpathy/MatlabWrapper/test/test1.cpp"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/MatlabWrapper/test/test1.cpp]
semantic-status: complete-named-text-read
---

# repos/karpathy/MatlabWrapper/test/test1.cpp

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/MatlabWrapper/test/test1.cpp), SHA-256 `34eb905a7212d370862485f4a4f73633a5b9b9079d5a8189b669b59b96a93d02`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt:

```text
#include <stdlib.h> #include <stdio.h> #include <string.h> #include <iostream> #include <Eigen/Eigen> #include <MatlabWrapper/MatlabWrapper.h> using namespace std;
```

MatlabWrapper header implementation and interactive example fully read, credited Karpathy August2012 BSD. Minimal Eigen float matrix bridge lazily starts MATLAB engine, transfers numeric copies, receives2D single/double with explicit cast, executes commands and interactive qq exit, and visualizes then retrieves random matrix. Ownership cleanup explicit for mxArray copies. Historical limits: constructor leaves engine pointer uninitialized but destructor closes it, lazy init failure not checked, receive/exec/interact assume init, old dimension-pointer API, no automated equality assertion in test. Convenience visualization workflow, no current dependency installation or execution.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <iostream>

#include <Eigen/Eigen>
#include <MatlabWrapper/MatlabWrapper.h>

using namespace std;
int main()
{
	
	Eigen::MatrixXf X = Eigen::MatrixXf::Random(10, 10);
	cout << "generated random matrix. It is " << X << endl;
	
	MatlabWrapper mw;
	mw.sendMat("X", X); 	// move matrix X to Matlab Engine under variable name X
	mw.exec("imshow(X, [])", true); // display it and wait for user to hit Enter
	mw.exec("close"); // close the figure
	
	// start an interactive session. Use Matlab as normal!
	// feel free to modify the matrix X we sent over. We will retrieve it back
	mw.interact();
	
	Eigen::MatrixXf mat;
  mw.receiveMat("X", mat);
	cout << "retrieving matrix X back. It is " << mat << endl;
	
	return 0;
}



```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
