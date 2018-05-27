<span><a class="tar_download_link" href="https://github.com/cristianduque/LanPlot/tarball/master">Download tar.gz file</a> | <a class="zip_download_link" href="https://github.com/cristianduque/LanPlot/archive/master.zip">Download zip file </a></span>

<h1> LanPlot </h1>

<h3> Introduction </h3>

LanPlot is a new programming language designed to find and plot the Fourier Transform of a given signal. Fourier Series are used to approximate in a periodic way any signal, and its transform is a decomposition of that same signal into frequencies. The motivation for designing this language was to make it easier to visualize the behavior of different signals used specially in communications. LanPlot will be able to take expressions expressed as signals or variables, compute their Fourier Transform, and plot them. A projection for this language is to make possible to plot the square, sawtooth, and triangle Fourier Series approximations of different signals accordingly. 

<h3> Language Feautures </h3>

The main idea for this language is to make graphs of the Fourier Transform of signals used in communications. It takes a signal as direct input or as a variable and plots its Fourier transform over a specified number of samples. A variable in this program can hold a signal expressed as an exponential, cosine or sine. In other words, a variable can be a function. An important detail is that every variable or function to plot has to be accompanied by a parameter corresponding to the number of samples to plot. Throughout the development of this programming language, changes to instructions and features will be made. 

<h3>Example of Program</h3>

LanPlot can take inputs in the following ways:
```
•	PLOT FOURIERTRANSFORM signal, number_of_samples
•	PLOT FOURIERTRANSFORM variable
•	variable = signal, number_of_samples
•	variable = FOURIERTRANSFORM variable
•	PLOT variable
•	variable = variable

```
An example of a program could be: 
```
 #(LanPlot) > var = cos(2*pi*50*t), 600
#var
#(LanPlot) > plot fouriertransform var //output graph is generated

```
<h3> LanPlot Demo </h3>
<iframe width="560" height="315" src="https://www.youtube.com/watch?v=xqD7CVC3tUc" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
