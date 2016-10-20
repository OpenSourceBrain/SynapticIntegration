/*****

A file to create info widgets, plots, save variables etc. in OSB

*****/

/////////////    Info

var Popup1 = G.addWidget(Widgets.POPUP);
Popup1.setMessage("Layer 2/3 pyramidal cell model from the <a target='_blank' href='https://bbp.epfl.ch/nmc-portal/microcircuit'>Blue Brain Project's Neocortical Microcircuit Collaboration Portal</a>.<br/><br/> The <b>original OSB project</b> for this model is <a target='_blank' href='http://opensourcebrain.org/projects/blue-brain-project-showcase'>here</a>.");
Popup1.setName("Description");
Popup1.setPosition(1074,142)
Popup1.setSize(391.8,454.8)


////////////   Watch


Instances.getInstance("TimedSyns.popL23[0].Seg0_soma_0_0.v");
TimedSyns.popL23[0].Seg0_soma_0_0.v.setWatched(true);

Instances.getInstance("TimedSyns.popL23[0].Seg0_dend_21_264.v");
TimedSyns.popL23[0].Seg0_dend_21_264.v.setWatched(true);
Instances.getInstance("TimedSyns.popL23[0].Seg40_dend_27_340.v");
TimedSyns.popL23[0].Seg40_dend_27_340.v.setWatched(true);



/////////////  Plot

var Plot1 = G.addWidget(Widgets.PLOT);
Plot1.setName("Membrane potentials");

Plot1.setPosition(120, 90);
Plot1.setSize(230,465);

Plot1.plotData(TimedSyns.popL23[0].Seg0_soma_0_0.v);
Plot1.setLegend(TimedSyns.popL23[0].Seg0_soma_0_0.v,"Soma");
Plot1.plotData(TimedSyns.popL23[0].Seg0_dend_21_264.v);
Plot1.setLegend(TimedSyns.popL23[0].Seg0_dend_21_264.v,"Basal - prox");
Plot1.plotData(TimedSyns.popL23[0].Seg40_dend_27_340.v);
Plot1.setLegend(TimedSyns.popL23[0].Seg40_dend_27_340.v,"Basal - dist");


