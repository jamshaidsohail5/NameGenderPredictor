Forked Stephen Holiday's (Special Thanks & Kudos to him) project and migrated for Python3.5 for learning purpose.

```plain
name.pickle exists, loading data
name.pickle loaded
32031 males names loaded, 56347 female loaded

Accuracy: 0.9692803801765105

Most Informative Features
	 last_three = INA 
	 last_two = CK 
	 last_three = CIA 
	 last_three = ENA 
	 last_three = NNA 
	 last_three = IRA 
	 last_three = ICK 
	 last_three = SIA 
	 last_three = TTA 
	 last_three = ICA 
   
 <<<  Testing Module   >>> 
Enter "q" or "quit" to end testing module
Enter name to classify: vijay
vijay is classified as M
Enter name to classify: anand
anand is classified as M
Enter name to classify: anna
anna is classified as F
Enter name to classify: uma
uma is classified as F
Enter name to classify: quit
End
```

Please feel free to SHARE YOUR THOUGHTS !!

# genderPredictor #
GenderPredictor is a wrapper around [NLTK](http://www.nltk.org/)'s [Naive Bayes](http://en.wikipedia.org/wiki/Naive_Bayes_classifier) classifier for predicting the gender given a name.

This problem is common when dealing with incomplete contact information for users.

Currently it appears to be about 82% accurate on American names but this is just the framework.
The name files are from the [US Social Security Administration](http://www.ssa.gov/oact/babynames/limits.html) and are likely in the public domain. The processed files are distributed under the same rules as the original data (which is likely public domain...).

The code is under the [Apache 2.0](http://www.apache.org/licenses/LICENSE-2.0) license.

Comments and suggestions are welcome at [stephen.holiday@gmail.com](mailto:stephen.holiday@gmail.com),

Stephen Holiday
[stephenholiday.com](http://stephenholiday.com)
