import tensorflow as tf

from django.shortcuts import render

from HandwritingWeb.NN.src.Model import Model, DecoderType
from HandwritingWeb.NN.src.main import infer
from HandwritingWeb.form import ImageForm
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

fnCharList = 'HandwritingWeb/NN/model/charList.txt'
fnInfer = 'media/photoNumber/line.png'


def HandwritingView(request):
    if request.method == 'POST':
        i_form = ImageForm(request.POST, request.FILES)
        if i_form.is_valid() and i_form.instance.photo.name is not None:
            i_form.save()
            photo = i_form.instance.photo.name
            filename = f'media/{photo}'
            tf.compat.v1.reset_default_graph()
            model = Model(list(open(fnCharList).read()), decoderType=DecoderType.BestPath,
                          mustRestore=True)
            answerNN = infer(model, filename)

            answer = answerNN
            return render(request, "HandwritingWeb/resul2.html", {'answer': answer, 'filename': filename})
        else:
            i_form = ImageForm()
            return render(request, "HandwritingWeb/handwriting.html", {'i_form': i_form})
    else:
        i_form = ImageForm()
    return render(request, "HandwritingWeb/handwriting.html", {'i_form': i_form})


def ResultView(request):
    return render(request, "HandwritingWeb/resul2.html")


def AboutProgramView(request):
    return render(request, "HandwritingWeb/about_program.html")
