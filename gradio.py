import gradio as gr
#from pathlib import Path
def wav2vec2(inputs):
    print("AUDIO::",inputs)
    
   # path=inputs.name
    #print("PATH::",path)
    #qq=Path(str(path))
    
    #audio_input, _ = sf.read(qq)
    #input_values = tokenizer(audio_input, return_tensors="pt").input_values
    #logits = model(input_values).logits
    #predicted_ids = torch.argmax(logits, dim=-1)
    #return tokenizer.batch_decode(predicted_ids)[0]
    return 'danu'
inputs = gr.inputs.Audio(source="microphone",type='file')

outputs =  gr.outputs.Textbox(label="Output Text")
gr.Interface(wav2vec2, inputs=inputs,outputs=outputs).launch()
