---
type: source
subject: "GitHub source repos/karpathy/EigenLibSVM/include/eigenlibsvm/svm_utils.h"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/EigenLibSVM/include/eigenlibsvm/svm_utils.h]
semantic-status: complete-named-text-read
---

# repos/karpathy/EigenLibSVM/include/eigenlibsvm/svm_utils.h

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/EigenLibSVM/include/eigenlibsvm/svm_utils.h), SHA-256 `da6690253b62a122266a8985103caec76a9f34270ba918416bd078176e3d9985`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt:

```text
/* Author: Andrej Karpathy (http://cs.stanford.edu/~karpathy/) 1 May 2012 BSD licence */ #ifndef __EIGEN_SVM_UTILS_H__ #define __EIGEN_SVM_UTILS_H__
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

#ifndef __EIGEN_SVM_UTILS_H__
#define __EIGEN_SVM_UTILS_H__

#include <string>
#include <vector>
#include <libsvm/svm.h>
#include <eigen3/Eigen/Eigen>

using namespace std;
namespace esvm {
  
  /* 
  Trains a binary SVM on dense data with linear kernel using libsvm. 
  Usage:
  
  vector<int> yhat;
  SVMClassifier svm;
  svm.train(X, y);
  svm.test(X, yhat);

  where X is an Eigen::MatrixXf that is NxD array. (N D-dimensional data),
  y is a vector<int> or an Eigen::MatrixXf Nx1 vector. The labels are assumed
  to be -1 and 1. This version doesn't play nice if your dataset is 
  too unbalanced.
  */
  class SVMClassifier{
    public:
      
      SVMClassifier();
      ~SVMClassifier();
      
      // train the svm
      void train(const Eigen::MatrixXf &X, const vector<int> &y);
      void train(const Eigen::MatrixXf &X, const Eigen::MatrixXf &y);
      
      // test on new data 
      void test(const Eigen::MatrixXf &X, vector<int> &yhat);
      
      // libsvm does not directly calculate the w and b, but a set of support
      // vectors. This function will use them to compute w and b, as currenly
      // we assume linear kernel only
      // yhat = sign( X * w + b )
      void getw(Eigen::MatrixXf &w, float &b);
      
      // I/O
      int saveModel(const char *filename);
      void loadModel(const char *filename); 
      
      // options
      void setC(double Cnew); //default is 1.0
      
      //TODO: add cross validation support
      //TODO: add probability support?
      
    protected:
    
      svm_model *model_;
      svm_problem *problem_;
      svm_parameter *param_;
      svm_node *x_space_;
      
      int D_; //dimension of data
  };
};


#endif //__EIGEN_SVM_UTILS_H__

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
