# Data analysis of the Netflix shows - part 2
##### Date: 04/12/2020
##### Time: 12:30-14:30

## Text analysis
Natural Language Processing (NLP) is about developing applications and services that can understand human languages.
Nowadays we have millions of gigabytes of data generated every day by blogs, social websites, and web pages. A big data analysis using NLP applications can turn out to be very beneficial. Possible NLP applications are speech recognition/translation, semantic analysis of the words, the syntactical/grammatical analysis of the sentences and paragraphs, and others. The analysis of the text is a common and main task in NLP.
We will focus on some basic text analysis operations and how are they performed using Python.

<div class="a-box notes-box">
<b>Note:</b><br>
If you are interested in a further application of NLP methods in python (beyond the materials of this lesson), I suggest you to read the following article: <a href="https://medium.com/towards-artificial-intelligence/text-mining-in-python-steps-and-examples-78b3f8fd913b">https://medium.com/towards-artificial-intelligence/text-mining-in-python-steps-and-examples-78b3f8fd913b</a>
</div>

## The NLTK library
The Natural language toolkit (NLTK) is a very popular library for natural language processing in python and it has a large active community behind it. We need to install it:

<code class="py important">pip3 install nltk</code>

To check if the NLTK library has been correctly installed we need to import it in our python script:

<code class="py important">Import nltk</code>

If every thing looks fine we will install/download popular nltk packages. We will download the popular and essential ones used for working with the basic nltk operations. Write the following line in your python script (after importing nltk):

<code class="py important">nltk.download("popular")</code>

<div class="a-box notes-box">
<b>Note:</b><br>
In case running the above commands returns an error message: <b><i>"CERTIFICATE_VERIFY_FAILED"</i></b>, then write in your script only the following lines and run it again.

<div class="py-hint-box large">
<div class="code-sec large">
<span>import nltk</span><hr>
<span>import ssl</span><hr>
<span></span><hr>
<span>try:</span><hr>
<span>&nbsp;&nbsp;&nbsp;&nbsp;_create_unverified_https_context = ssl._create_unverified_context</span><hr>
<span>except AttributeError:</span><hr>
<span>&nbsp;&nbsp;&nbsp;&nbsp;pass</span><hr>
<span>else:</span><hr>
<span>&nbsp;&nbsp;&nbsp;&nbsp;ssl._create_default_https_context = _create_unverified_https_context</span><hr>
<span></span><hr>
<span>nltk.download()</span><hr>
</div>
</div>

If you still have some errors please follow these instructions <a href="https://www.xspdf.com/help/50406704.html">https://www.xspdf.com/help/50406704.html</a>
</div>

## Tokenization and stopwords removal
First thing we want to do is a **Tokenization** and **Stopwords removal**.

**Tokenization** is the process of separating and classifying different sections of a string. The resulting tokens are then passed on to some other form of processing.
<div class="a-box notes-box">
<b>For example:</b><br><br>
If we want to tokenize the sentence <br><b><i>"Hi I am Marco and I am a DHDK student"</i></b><br><br>    
Our list of tokens would be:<br><i><b>"Hi", "I", "am", "Marco", "and", "I", "am", "a", "DHDK", "student"</b></i>
</div>

**Stopwords removal** these are words that may not carry any valuable information, like articles (e.g. "the"), conjunctions (e.g. "and"), or propositions (e.g. "with").
<div class="a-box notes-box">
<b>For example:</b><br><br>
If we want to remove the stop words from the list of tokens <br><i><b>"Hi", "I", "am", "Marco", "and", "I", "am", "a", "DHDK", "student"</b></i> <br><br>
Then our new list could be:<br> <i><b>"Hi", "Marco", "DHDK", "student"</b></i>
</div>

## Toward a text analysis of the Netflix shows dataset <span class="inline-header">(see also the [github repository](https://github.com/comp-think/2020-2021/tree/master/docs/laboratory/src/lessons/6_7))</span>
Lets see an example in python first
<div class="py-hint-box large">
<div class="code-sec large">
<span>from nltk.corpus import stopwords</span><hr>
<span>from nltk.tokenize import word_tokenize</span><hr>
<span></span><hr>
<span>example_sent = "I want to tokenize and remove all the stopwords from this sentence"</span><hr>
<span></span><hr>
<span class="comment"># Tokenize the given sentence</span><hr>
<span>word_tokens = word_tokenize(example_sent)</span><hr>
<span></span><hr>
<span class="comment"># Filter the stopwords</span><hr>
<span>stop_words = set(stopwords.words('english'))</span><hr>
<span>filtered_sentence = []</span><hr>
<span>for w in word_tokens:</span><hr>
<span>&nbsp;&nbsp;&nbsp;&nbsp;if not w in stop_words:</span><hr>
<span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;filtered_sentence.append(w)</span><hr>
<span></span><hr>
<span>print(filtered_sentence</span><hr>
</div>  
</div>

<span class="inline-header">a)</span> define a function <code class="py">netflix_titles_tokens()</code> which returns a collection of all the different tokens/words in the Netflix shows titles. The collection should not include the stopwords.
<div class="py-hint-box large">
  Mark the box to see the solution
  <div class="code-sec large solution">
  <span>from nltk.corpus import stopwords</span><hr>
  <span>from nltk.tokenize import word_tokenize</span><hr>
  <span></span><hr>
  <span>def netflix_titles_tokens():</span><hr>
  <span>&nbsp;&nbsp;&nbsp;&nbsp;stop_words = set(stopwords.words('english'))</span><hr>
  <span>&nbsp;&nbsp;&nbsp;&nbsp;result = set()</span><hr>
  <span>&nbsp;&nbsp;&nbsp;&nbsp;for show in netflix_data:</span><hr>
  <span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;word_tokens = word_tokenize(show["title"])</span><hr>
  <span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;filtered_sentence = []</span><hr>
  <span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;for w in word_tokens:</span><hr>
  <span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if not w in stop_words:</span><hr>
  <span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;filtered_sentence.append(w)</span><hr>
  <span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;result.update(filtered_sentence)</span><hr>
  <span>&nbsp;&nbsp;&nbsp;&nbsp;return result</span><hr>
  <span></span><hr>
  <span>print(netflix_titles_tokens())</span><hr>
  </div>
</div>

<span class="inline-header">b)</span> define a function <code class="py">netflix_director_names()</code> which returns a collection of all the tokens/words included in the director field of the Netflix shows dataset. Each token must be accompanied with a number representing its frequency in the dataset.
<div class="a-box notes-box">
<b>Hint:</b><br>
Importing <code class="py">from nltk.probability import FreqDist</code> and using <code class="py">FreqDist({LIST_OF_TOKENS})</code> returns a dictionary, such that the dictionary key is a token and its value is the number of times it appears in the given list. To print the results you can use
<code class="py">{FREQ_DIST_DICT}.most_common({N})</code>, this function prints the {N} most frequent terms inside the dictionary {FREQ_DIST_DICT}.
<br><br>

<b>For example:</b><br>
<code class="py">FreqDist(["hi","bye","ciao","bye","hi"])</code> returns <code class="py">{"hi": 2, "bye":2, "ciao": 1}</code>

</div>  

<div class="py-hint-box large">
  Mark the box to see the solution
  <div class="code-sec large solution">
    <span>from nltk.probability import FreqDist</span><hr>
    <span></span><hr>
    <span>def netflix_director_names():</span><hr>
    <span>&nbsp;&nbsp;&nbsp;&nbsp;result = []</span><hr>
    <span>&nbsp;&nbsp;&nbsp;&nbsp;for show in netflix_data:</span><hr>
    <span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;word_tokens = word_tokenize(show["director"])</span><hr>
    <span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;result += word_tokens</span><hr>
    <span>&nbsp;&nbsp;&nbsp;&nbsp;return FreqDist(result)</span><hr>
    <span></span><hr>
    <span>counts = netflix_director_names()</span><hr>
  </div>
</div>
