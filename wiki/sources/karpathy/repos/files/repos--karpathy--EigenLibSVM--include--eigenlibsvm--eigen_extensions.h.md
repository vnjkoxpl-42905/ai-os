---
type: source
subject: "GitHub source repos/karpathy/EigenLibSVM/include/eigenlibsvm/eigen_extensions.h"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/EigenLibSVM/include/eigenlibsvm/eigen_extensions.h]
semantic-status: complete-named-text-read
---

# repos/karpathy/EigenLibSVM/include/eigenlibsvm/eigen_extensions.h

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/EigenLibSVM/include/eigenlibsvm/eigen_extensions.h), SHA-256 `dac96a6389c20ddac1e82c0f1e35aad781c4640c2767e37111edee21a2250c82`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt: "// Written by Alex Teichman (http://cs.stanford.edu/people/teichman/) #ifndef EIGEN_EXTENSIONS_H #define EIGEN_EXTENSIONS_H #include <stdint.h> #include <fstream> #include".

EigenLibSVM Karpathy-authored 2012 wrappers translate dense Eigen rows into LibSVM nodes, validate data/label dimensions and parameters, expose linear weights, C and model persistence, and explicitly warn about imbalance and missing cross-validation. Test prints expected MATLAB margins and approximately 0.945 training accuracy before and after save/load, rather than claiming held-out evaluation. Prediction allocates D nodes without the required terminating sentinel; source is historical and not correctness-certified. Matrix serialization helper credits Alex Teichman and notes newline-dependent ASCII parsing, so it is third-party evidence. Find-birds separates bounded depth-one acquisition with disk pickle caching and manual Tweepy error waits from offline recommendation: mutual-follow counts discounted by logarithmic popularity, expensive formatting only after top-list selection, then a plain HTML report. Incomplete cached users are explicitly skipped; remote descriptions inserted without escaping are a rendering limitation. These scripts were read without executing credentials, network collection or pickle payloads.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
// Written by Alex Teichman (http://cs.stanford.edu/people/teichman/)

#ifndef EIGEN_EXTENSIONS_H
#define EIGEN_EXTENSIONS_H

#include <stdint.h>
#include <fstream>
#include <iostream>

#include <eigen3/Eigen/Eigen>

namespace eigen_extensions {

  template<class S, int T, int U>
    void save(const Eigen::Matrix<S, T, U>& mat, const std::string& filename);

  template<class S, int T, int U>
    void load(const std::string& filename, Eigen::Matrix<S, T, U>* mat);

  template<class S, int T, int U>
    void serialize(const Eigen::Matrix<S, T, U>& mat, std::ostream& strm);
  
  template<class S, int T, int U>
    void deserialize(std::istream& strm, Eigen::Matrix<S, T, U>* mat);

  template<class S, int T, int U>
    void saveASCII(const Eigen::Matrix<S, T, U>& mat, const std::string& filename);

  //! TODO: Requires a newline at the end of the file.  Hand-made files might not have this.
  template<class S, int T, int U>
    void loadASCII(const std::string& filename, Eigen::Matrix<S, T, U>* mat);

  template<class S, int T, int U>
    void serializeASCII(const Eigen::Matrix<S, T, U>& mat, std::ostream& strm);
  
  template<class S, int T, int U>
    void deserializeASCII(std::istream& strm, Eigen::Matrix<S, T, U>* mat);



  

  template<class S, int T, int U>
    void serialize(const Eigen::Matrix<S, T, U>& mat, std::ostream& strm)
  {
    int bytes = sizeof(S);
    int rows = mat.rows();
    int cols = mat.cols();
    strm.write((char*)&bytes, sizeof(int));
    strm.write((char*)&rows, sizeof(int));
    strm.write((char*)&cols, sizeof(int));
    strm.write((const char*)mat.data(), sizeof(S) * rows * cols);
  }
    
  template<class S, int T, int U>
    void save(const Eigen::Matrix<S, T, U>& mat, const std::string& filename)
  {
    //assert(boost::filesystem::extension(filename).compare(".eig") == 0);
    std::ofstream file;
    file.open(filename.c_str());
    assert(file);
    serialize(mat, file);
    file.close();
  }
 
  template<class S, int T, int U>
    void deserialize(std::istream& strm, Eigen::Matrix<S, T, U>* mat)
  {
    int bytes;
    int rows;
    int cols;
    strm.read((char*)&bytes, sizeof(int));
    strm.read((char*)&rows, sizeof(int));
    strm.read((char*)&cols, sizeof(int));
    assert(bytes == sizeof(S));
      
    S *buf = (S*) malloc(sizeof(S) * rows * cols);
    strm.read((char*)buf, sizeof(S) * rows * cols);
    *mat = Eigen::Map< Eigen::Matrix<S, T, U> >(buf, rows, cols);
    free(buf);    
  }

  template<class S, int T, int U>
    void load(const std::string& filename, Eigen::Matrix<S, T, U>* mat)
  {
    //assert(boost::filesystem::extension(filename).compare(".eig") == 0);
    std::ifstream file;
    file.open(filename.c_str());
    if(!file)
      std::cerr << "File " << filename << " could not be opened.  Dying badly." << std::endl;
    assert(file);
    deserialize(file, mat);
    file.close();
  }


  /************************************************************
   * ASCII versions.
   ************************************************************/
  
  template<class S, int T, int U>
    void serializeASCII(const Eigen::Matrix<S, T, U>& mat, std::ostream& strm)
  {
    strm << mat << std::endl;
  }
    
  template<class S, int T, int U>
    void saveASCII(const Eigen::Matrix<S, T, U>& mat, const std::string& filename)
  {
    assert(filename.substr(filename.size() - 8).compare(".eig.txt") == 0);
    std::ofstream file;
    file.open(filename.c_str());
    assert(file);
    serializeASCII(mat, file);
    file.close();
  }
  
  template<class S, int T, int U>
    void deserializeASCII(std::istream& strm, Eigen::Matrix<S, T, U>* mat)
  {
    // -- Determine number of rows and number of cols.
    int start = strm.tellg();
    int rows = 0;
    std::string line;
    std::vector<std::string> lines;
    while(getline(strm, line), !strm.eof()) { 
      ++rows;
      lines.push_back(line);
    }

    assert(!lines.empty());
    std::istringstream iss(lines[0]);
    int cols = 0;
    double buf;
    while(!iss.eof()) {
      iss >> std::skipws >> buf;
      ++cols;
    }

    // -- Read in the data.
    *mat = Eigen::Matrix<S, T, U>(rows, cols);
    strm.seekg(start);
    for(int y = 0; y < rows; ++y) {
      std::istringstream iss(lines[y]);
      for(int x = 0; x < cols; ++x) {
	iss >> mat->coeffRef(y, x);
      }
    }
  }

  template<class S, int T, int U>
    void loadASCII(const std::string& filename, Eigen::Matrix<S, T, U>* mat)
  {
    assert(filename.substr(filename.size() - 8).compare(".eig.txt") == 0);
    std::ifstream file;
    file.open(filename.c_str());
    if(!file)
      std::cerr << "File " << filename << " could not be opened.  Dying badly." << std::endl;
    assert(file);
    deserializeASCII(file, mat);
    file.close();
  }

}

#endif // EIGEN_EXTENSIONS_H

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
