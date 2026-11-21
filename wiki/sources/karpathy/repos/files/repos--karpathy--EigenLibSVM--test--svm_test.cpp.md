---
type: source
subject: "GitHub source repos/karpathy/EigenLibSVM/test/svm_test.cpp"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/EigenLibSVM/test/svm_test.cpp]
semantic-status: complete-named-text-read
---

# repos/karpathy/EigenLibSVM/test/svm_test.cpp

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/EigenLibSVM/test/svm_test.cpp), SHA-256 `7023f5ae464c4a8d25a6fb400e4cfd4a3f84054a365f6ec41ad4ec5e69bde34a`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt:

```text
/* Author: Andrej Karpathy (http://cs.stanford.edu/~karpathy/) 1 May 2012 BSD licence */ #include <string> #include <vector>
```

EigenLibSVM Karpathy-authored 2012 wrappers translate dense Eigen rows into LibSVM nodes, validate data/label dimensions and parameters, expose linear weights, C and model persistence, and explicitly warn about imbalance and missing cross-validation. Test prints expected MATLAB margins and approximately 0.945 training accuracy before and after save/load, rather than claiming held-out evaluation. Prediction allocates D nodes without the required terminating sentinel; source is historical and not correctness-certified. Matrix serialization helper credits Alex Teichman and notes newline-dependent ASCII parsing, so it is third-party evidence. Find-birds separates bounded depth-one acquisition with disk pickle caching and manual Tweepy error waits from offline recommendation: mutual-follow counts discounted by logarithmic popularity, expensive formatting only after top-list selection, then a plain HTML report. Incomplete cached users are explicitly skipped; remote descriptions inserted without escaping are a rendering limitation. These scripts were read without executing credentials, network collection or pickle payloads.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
/*
Author: Andrej Karpathy (http://cs.stanford.edu/~karpathy/)
1 May 2012
BSD licence
*/

#include <string>
#include <vector>
#include <stdlib.h>

#include <eigen3/Eigen/Eigen>
#include <eigenlibsvm/svm_utils.h>
#include <eigenlibsvm/eigen_extensions.h>

using namespace std;
using namespace esvm;

// run from build folder of the project (see path below)
int main (int argc, char** argv) {
  
  Eigen::MatrixXf X;
  Eigen::MatrixXf y;
  eigen_extensions::loadASCII("../test/svmtestx.eig.txt", &X);
  eigen_extensions::loadASCII("../test/svmtesty.eig.txt", &y);
  
  // Classify
  cout << X.topRows(5) << endl;
  cout << y.topRows(5) << endl;
  vector<int> yhat;
  SVMClassifier svm;
  svm.train(X, y);
  svm.test(X, yhat);
  
  Eigen::MatrixXf w;
  float b;
  svm.getw(w, b);
  Eigen::MatrixXf margin= ((X * w).array() + b).matrix(); // ahh eigen...
  
  // Evaluate accuracy and print results
  int match=0;
  for(int i=0;i<yhat.size();i++) {
    if(yhat[i]==(int)y(i)) match++; else printf("WRONG! ");
    printf("y= %d, yhat= %d margin= %f\n", (int)y(i), yhat[i], margin(i));
  }
  printf("MATLAB cross-check: last margin should be around -3.107\n");
  printf("Accuracy= %f. From MATLAB cross-check, expect this to be around 0.945\n", 1.0*match/yhat.size());
  
  // Save the model
  svm.saveModel("temp.svmmodel");
  
  // Test loading model in new instance of SVMClassifier
  SVMClassifier svm2;
  svm2.loadModel("temp.svmmodel");
  yhat.clear();
  svm2.test(X, yhat);
  match=0; 
  for(int i=0;i<yhat.size();i++) if(yhat[i]==(int)y(i)) match++;
  printf("Accuracy= %f from loaded model. Should be 0.945 again.\n", 1.0*match/yhat.size());
  
  
  printf("you may want to rm the temporary file temp.svmmodel\n");
}
  

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
