# Data analysis of the Netflix shows - part 3
##### Date: 11/12/2020
##### Time: 12:30-14:30

## Data visualization
<li>Apply a graphic representation on the data: mapping the original data to graphic elements (for example: lines, points, barchart etc).</li>
<li>If we want to draw a graphic on top of a dataset, we need to walk through these three steps:
  <ul>
    <li> What is the nature of our data?</li>  
    <li> What aspects we want to analyse?</li>
    <li> What are the most suitable graphical elements we can use to present our analysis?</li>
  </ul>
</li>

<div class="a-box notes-box">
<b>Example:</b>
<b>Data:</b> a collection of articles. For each article we have the year of its publication and the author/s.
<b>Analysis:</b> we want to check how many articles did "Silvio Peroni" authored on each different year.
<b>Visualization:</b> we can use a barchart.
<img src="../img/barchart.png">
</div>

## The matplotlib library
matplotlib was the first Python data visualization library and it's still widely used for plotting in the Python community. It was designed to closely resemble MATLAB, a popular proprietary programming language. <br>
We are especially interested in <code class="py">matplotlib.pyplot</code>, a collection of plotting functions. Each pyplot function makes some change to a figure: e.g., creates a figure, creates a plotting area in a figure, plots some lines in a plotting area, decorates the plot with labels, etc.<br><br>
<b>Note:</b> this is not a builtin library of python so we need to install it using <code class="py">pip install matplotlib</code>
<br>
<div class="py-hint-box large">
<div class="code-sec large">
<span>import matplotlib.pyplot as plt</span><hr>
<span></span><hr>
<span>data = [23,85, 72, 43, 52]</span><hr>
<span>labels = ['A', 'B', 'C', 'D', 'E']</span><hr>
<span></span><hr>
<span class="comment"># x-Axis ticks and label</span><hr>
<span>plt.xticks(range(len(data)), labels)</span><hr>
<span>plt.xlabel('Class')</span><hr>
<span></span><hr>
<span class="comment"># y-Axis label</span><hr>
<span>plt.ylabel('Amounts')</span><hr>
<span></span><hr>
<span class="comment"># chart title</span><hr>
<span>plt.title('I am title')</span><hr>
<span></span><hr>
<span class="comment"># plt a bar</span><hr>
<span>plt.bar(range(len(data)), data)</span><hr>
<span>plt.show(</span><hr>
</div>
</div>
After running the above script this chart should appear:
<img src="../img/matplotlib_1.png">

## Data visualizations on the Netflix shows dataset <span class="inline-header">(see also the [github repository](https://github.com/comp-think/2020-2021/tree/master/docs/laboratory/src/lessons/8))</span>

To answer the following exercises we need to use some of the functions we have defined on the previous lessons (part-1, and part-2).

<span class="inline-header">a)</span> Draw a graphic using <code class="py">matplotlib</code> which plots the total number of shows (all type of shows) that Netflix added for each different year.

<span class="inline-header">b)</span> Draw a graphic using <code class="py">matplotlib</code> which plots the average time (in years) it takes Netflix to add a show on its list after its actual release. Plot this value for each different year.<br>
<b>Hint: </b> Take a look at the line charts of matplotlib [https://datatofish.com/line-chart-python-matplotlib/](https://datatofish.com/line-chart-python-matplotlib/).
