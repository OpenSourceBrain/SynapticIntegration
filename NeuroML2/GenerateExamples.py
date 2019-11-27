from neuromllite import *
from neuromllite.NetworkGenerator import *
from neuromllite.utils import create_new_model
from pyneuroml.pynml import read_neuroml2_file
import sys

sys.path.append("..")

colors = {'PassiveCell':'0 0 0.8', 'cADpyr229_L23_PC_5ecbf9b163_0_0':'0.8 0 0', 'pyr_4_sym':'0 0 0.8', 'IB':'0.8 0 0', 'IBR':'0.8 0 0'}

def generate(cell, duration, config='IClamp'):
    
    reference = "%s_%s"%(config, cell)

    cell_id = '%s'%cell
    nml2_filename = '%s.cell.nml'%(cell)
    cell_nmll = Cell(id=cell_id, neuroml2_source_file=nml2_filename)
 
    ################################################################################
    ###   Add some inputs
    
    syn_exc = None
    
    if 'IClamp' in config:
        parameters = {}
        parameters['stim_amp'] = '350pA'
        parameters['stim_delay'] = '100ms'
        parameters['stim_dur'] = '500ms'
        input_source = InputSource(id='iclamp_0', 
                                   neuroml2_input='PulseGenerator', 
                                   parameters={'amplitude':'stim_amp', 'delay':'stim_delay', 'duration':'stim_dur'})
      
        
    elif 'Poisson' in config:
        syn_exc = Synapse(id='ampa', 
                              neuroml2_source_file='ampa.synapse.nml')
        parameters = {}
        parameters['average_rate'] = '100 Hz'
        parameters['number_per_cell'] = '10'
        input_source = InputSource(id='pfs0', 
                                   neuroml2_input='PoissonFiringSynapse', 
                                   parameters={'average_rate':'average_rate', 
                                               'synapse':syn_exc.id, 
                                               'spike_target':"./%s"%syn_exc.id})
                                               
    sim, net = create_new_model(reference,
                     duration, 
                     dt=0.01, # ms 
                     temperature=34, # degC
                     default_region='Cortex',
                     parameters = parameters,
                     cell_for_default_population=cell_nmll,
                     color_for_default_population=colors[cell],
                     input_for_default_population=input_source)
              
    if 'Poisson' in config:
        net.synapses.append(syn_exc)
        net.inputs[0].number_per_cell = 'number_per_cell'

                   
    cell = read_neuroml2_file(nml2_filename).cells[0]
    
    if len(cell.morphology.segments)>1:
        sim.recordVariables={}
        for seg in cell.morphology.segments:
            seg_id = seg.id
            if seg_id!=0 and seg_id%500<10:
                sim.recordVariables['%i/v'%seg_id]={'all':'*'}
        
    '''
    sim.recordVariables={'biophys/membraneProperties/Na_all/Na/m/q':{'all':'*'},
                         'biophys/membraneProperties/Na_all/Na/h/q':{'all':'*'},
                         'biophys/membraneProperties/Kd_all/Kd/n/q':{'all':'*'}}
    
    if cell != 'FS':
        sim.recordVariables['biophys/membraneProperties/IM_all/IM/p/q']={'all':'*'}
        
    if cell == 'IB' or cell == 'IBR':
        sim.recordVariables['biophys/membraneProperties/IL_all/IL/q/q']={'all':'*'}
        sim.recordVariables['biophys/membraneProperties/IL_all/IL/r/q']={'all':'*'}
        
    if cell == 'LTS':
        sim.recordVariables['biophys/membraneProperties/IT_all/IT/s/q']={'all':'*'}
        sim.recordVariables['biophys/membraneProperties/IT_all/IT/u/q']={'all':'*'}'''
        
    net.to_json_file()
    sim.to_json_file()

    return sim, net



if __name__ == "__main__":
    
    if '-all' in sys.argv:
        for cell in colors:
            generate('PassiveCell', 700, config="IClamp")
            generate('pyr_4_sym', 700, config="IClamp")
            generate('pyr_4_sym', 700, config="Poisson")
            generate('cADpyr229_L23_PC_5ecbf9b163_0_0', 700, config="IClamp")
            generate('cADpyr229_L23_PC_5ecbf9b163_0_0', 700, config="Poisson")
            
        
    else:
        #sim, net = generate('pyr_4_sym', 700, config="IClamp")
        sim, net = generate('pyr_4_sym', 700, config="Poisson")
        
        check_to_generate_or_run(sys.argv, sim)
    
