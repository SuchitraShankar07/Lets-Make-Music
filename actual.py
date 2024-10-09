{"metadata":{"kernelspec":{"language":"python","display_name":"Python 3","name":"python3"},"language_info":{"name":"python","version":"3.10.14","mimetype":"text/x-python","codemirror_mode":{"name":"ipython","version":3},"pygments_lexer":"ipython3","nbconvert_exporter":"python","file_extension":".py"},"kaggle":{"accelerator":"nvidiaTeslaT4","dataSources":[{"sourceId":2356848,"sourceType":"datasetVersion","datasetId":1423230}],"dockerImageVersionId":30787,"isInternetEnabled":true,"language":"python","sourceType":"notebook","isGpuEnabled":true}},"nbformat_minor":4,"nbformat":4,"cells":[{"cell_type":"code","source":"!pip install music21","metadata":{"_uuid":"8f2839f25d086af736a60e9eeb907d3b93b6e0e5","_cell_guid":"b1076dfc-b9ad-4769-8c92-a6c4dae69d19","execution":{"iopub.status.busy":"2024-10-09T19:25:57.675674Z","iopub.execute_input":"2024-10-09T19:25:57.676521Z","iopub.status.idle":"2024-10-09T19:26:16.931759Z","shell.execute_reply.started":"2024-10-09T19:25:57.676480Z","shell.execute_reply":"2024-10-09T19:26:16.930532Z"},"trusted":true},"execution_count":5,"outputs":[{"name":"stdout","text":"Collecting music21\n  Downloading music21-9.1.0-py3-none-any.whl.metadata (4.8 kB)\nCollecting chardet (from music21)\n  Downloading chardet-5.2.0-py3-none-any.whl.metadata (3.4 kB)\nRequirement already satisfied: joblib in /opt/conda/lib/python3.10/site-packages (from music21) (1.4.2)\nCollecting jsonpickle (from music21)\n  Downloading jsonpickle-3.3.0-py3-none-any.whl.metadata (8.3 kB)\nRequirement already satisfied: matplotlib in /opt/conda/lib/python3.10/site-packages (from music21) (3.7.5)\nRequirement already satisfied: more-itertools in /opt/conda/lib/python3.10/site-packages (from music21) (10.3.0)\nRequirement already satisfied: numpy in /opt/conda/lib/python3.10/site-packages (from music21) (1.26.4)\nRequirement already satisfied: requests in /opt/conda/lib/python3.10/site-packages (from music21) (2.32.3)\nRequirement already satisfied: webcolors>=1.5 in /opt/conda/lib/python3.10/site-packages (from music21) (24.6.0)\nRequirement already satisfied: contourpy>=1.0.1 in /opt/conda/lib/python3.10/site-packages (from matplotlib->music21) (1.2.1)\nRequirement already satisfied: cycler>=0.10 in /opt/conda/lib/python3.10/site-packages (from matplotlib->music21) (0.12.1)\nRequirement already satisfied: fonttools>=4.22.0 in /opt/conda/lib/python3.10/site-packages (from matplotlib->music21) (4.53.0)\nRequirement already satisfied: kiwisolver>=1.0.1 in /opt/conda/lib/python3.10/site-packages (from matplotlib->music21) (1.4.5)\nRequirement already satisfied: packaging>=20.0 in /opt/conda/lib/python3.10/site-packages (from matplotlib->music21) (21.3)\nRequirement already satisfied: pillow>=6.2.0 in /opt/conda/lib/python3.10/site-packages (from matplotlib->music21) (10.3.0)\nRequirement already satisfied: pyparsing>=2.3.1 in /opt/conda/lib/python3.10/site-packages (from matplotlib->music21) (3.1.2)\nRequirement already satisfied: python-dateutil>=2.7 in /opt/conda/lib/python3.10/site-packages (from matplotlib->music21) (2.9.0.post0)\nRequirement already satisfied: charset-normalizer<4,>=2 in /opt/conda/lib/python3.10/site-packages (from requests->music21) (3.3.2)\nRequirement already satisfied: idna<4,>=2.5 in /opt/conda/lib/python3.10/site-packages (from requests->music21) (3.7)\nRequirement already satisfied: urllib3<3,>=1.21.1 in /opt/conda/lib/python3.10/site-packages (from requests->music21) (1.26.18)\nRequirement already satisfied: certifi>=2017.4.17 in /opt/conda/lib/python3.10/site-packages (from requests->music21) (2024.8.30)\nRequirement already satisfied: six>=1.5 in /opt/conda/lib/python3.10/site-packages (from python-dateutil>=2.7->matplotlib->music21) (1.16.0)\nDownloading music21-9.1.0-py3-none-any.whl (22.8 MB)\n\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m22.8/22.8 MB\u001b[0m \u001b[31m55.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m:00:01\u001b[0m00:01\u001b[0m\n\u001b[?25hDownloading chardet-5.2.0-py3-none-any.whl (199 kB)\n\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m199.4/199.4 kB\u001b[0m \u001b[31m14.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n\u001b[?25hDownloading jsonpickle-3.3.0-py3-none-any.whl (42 kB)\n\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m42.4/42.4 kB\u001b[0m \u001b[31m2.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n\u001b[?25hInstalling collected packages: jsonpickle, chardet, music21\nSuccessfully installed chardet-5.2.0 jsonpickle-3.3.0 music21-9.1.0\n","output_type":"stream"}]},{"cell_type":"code","source":"import glob\nimport pickle\nimport numpy\nfrom music21 import converter, instrument, note, chord\nfrom keras.models import Sequential\nfrom keras.layers import Dense\nfrom keras.layers import Dropout\nfrom keras.layers import LSTM\nfrom keras.layers import Activation\nfrom keras.layers import BatchNormalization as BatchNorm\nfrom tensorflow.keras.utils import to_categorical\nfrom keras.callbacks import ModelCheckpoint","metadata":{"execution":{"iopub.status.busy":"2024-10-09T19:26:16.934115Z","iopub.execute_input":"2024-10-09T19:26:16.934511Z","iopub.status.idle":"2024-10-09T19:26:30.799466Z","shell.execute_reply.started":"2024-10-09T19:26:16.934460Z","shell.execute_reply":"2024-10-09T19:26:30.798622Z"},"trusted":true},"execution_count":6,"outputs":[]},{"cell_type":"code","source":"def get_notes():\n    notes = []\n\n    for file in glob.glob(\"../input/lakh-midi-clean/10cc/*.mid\"):\n        midi = converter.parse(file)\n\n        print(\"Parsing %s\" % file)\n\n        parsing_notes = None\n\n        try: \n            s2 = instrument.partitionByInstrument(midi)\n            parsing_notes = s2.parts[0].recurse() \n        except: \n            parsing_notes = midi.flat.notes\n\n        for unit in parsing_notes:\n            if isinstance(unit, note.Note):\n                notes.append(str(unit.pitch))\n            elif isinstance(unit, chord.Chord):\n                notes.append('.'.join(str(n) for n in unit.normalOrder))\n\n    with open('./notes', 'wb') as filepath:\n        pickle.dump(notes, filepath)\n        \n    return notes\n        \n","metadata":{"execution":{"iopub.status.busy":"2024-10-09T19:26:30.800931Z","iopub.execute_input":"2024-10-09T19:26:30.801700Z","iopub.status.idle":"2024-10-09T19:26:30.811063Z","shell.execute_reply.started":"2024-10-09T19:26:30.801645Z","shell.execute_reply":"2024-10-09T19:26:30.810084Z"},"trusted":true},"execution_count":7,"outputs":[]},{"cell_type":"code","source":"def prepare_sequences(notes, n_vocab):\n \n    sequence_length = 100\n    name_of_pitch = sorted(set(item for item in notes))\n    note_to_int = dict((note, number) for number, note in enumerate(name_of_pitch))\n\n    inputs_model = []\n    output_model = []\n\n    # create input sequences and the corresponding outputs\n    for i in range(0, len(notes) - sequence_length, 1):\n        sequence_in = notes[i:i + sequence_length]\n        sequence_out = notes[i + sequence_length]\n        inputs_model.append([note_to_int[char] for char in sequence_in])\n        output_model.append(note_to_int[sequence_out])\n\n    n_patterns = len(inputs_model)\n\n    # reshape the input into a format compatible with LSTM layers\n    inputs_model = numpy.reshape(inputs_model, (n_patterns, sequence_length, 1))\n    # normalize input\n    inputs_model = inputs_model / float(n_vocab)\n\n    output_model = to_categorical(output_model)\n\n    return (inputs_model, output_model)","metadata":{"execution":{"iopub.status.busy":"2024-10-09T19:26:30.812399Z","iopub.execute_input":"2024-10-09T19:26:30.812744Z","iopub.status.idle":"2024-10-09T19:26:30.842747Z","shell.execute_reply.started":"2024-10-09T19:26:30.812707Z","shell.execute_reply":"2024-10-09T19:26:30.841759Z"},"trusted":true},"execution_count":8,"outputs":[]},{"cell_type":"code","source":"def create_network(inputs_model, n_vocab):\n    model = Sequential()\n    model.add(LSTM(\n        512,\n        input_shape=(inputs_model.shape[1], inputs_model.shape[2]),\n        recurrent_dropout=0.3,\n        return_sequences=True\n    ))\n    model.add(LSTM(512, return_sequences=True, recurrent_dropout=0.3,))\n    model.add(LSTM(512))\n    model.add(BatchNorm())\n    model.add(Dropout(0.3))\n    model.add(Dense(256))\n    model.add(Activation('relu'))\n    model.add(BatchNorm())\n    model.add(Dropout(0.3))\n    model.add(Dense(n_vocab))\n    model.add(Activation('softmax'))\n    model.compile(loss='categorical_crossentropy', optimizer='rmsprop')\n\n    return model","metadata":{"execution":{"iopub.status.busy":"2024-10-09T19:26:30.845744Z","iopub.execute_input":"2024-10-09T19:26:30.846153Z","iopub.status.idle":"2024-10-09T19:26:30.854768Z","shell.execute_reply.started":"2024-10-09T19:26:30.846107Z","shell.execute_reply":"2024-10-09T19:26:30.853870Z"},"trusted":true},"execution_count":9,"outputs":[]},{"cell_type":"code","source":"def train(model, inputs_model, output_model):\n    filepath = \"weights-improvement-{epoch:02d}-{loss:.4f}-bigger.keras\"\n    checkpoint = ModelCheckpoint(\n        filepath,\n        monitor='loss',\n        verbose=0,\n        save_best_only=True,\n        mode='min'\n    )\n    callbacks_list = [checkpoint]\n\n    model.fit(inputs_model, output_model, epochs=200, batch_size=128, callbacks=callbacks_list)","metadata":{"execution":{"iopub.status.busy":"2024-10-09T19:26:30.856007Z","iopub.execute_input":"2024-10-09T19:26:30.856341Z","iopub.status.idle":"2024-10-09T19:26:30.863675Z","shell.execute_reply.started":"2024-10-09T19:26:30.856307Z","shell.execute_reply":"2024-10-09T19:26:30.862827Z"},"trusted":true},"execution_count":10,"outputs":[]},{"cell_type":"code","source":"def train_network():\n    notes = get_notes()\n    n_vocab = len(set(notes))\n    inputs_model, output_model = prepare_sequences(notes, n_vocab)\n    model = create_network(inputs_model, n_vocab)\n    train(model, inputs_model, output_model)\n","metadata":{"execution":{"iopub.status.busy":"2024-10-09T19:26:30.865020Z","iopub.execute_input":"2024-10-09T19:26:30.865753Z","iopub.status.idle":"2024-10-09T19:26:30.872475Z","shell.execute_reply.started":"2024-10-09T19:26:30.865704Z","shell.execute_reply":"2024-10-09T19:26:30.871639Z"},"trusted":true},"execution_count":11,"outputs":[]},{"cell_type":"code","source":"train_network()","metadata":{"execution":{"iopub.status.busy":"2024-10-09T19:26:30.873688Z","iopub.execute_input":"2024-10-09T19:26:30.874061Z"},"trusted":true},"execution_count":null,"outputs":[{"name":"stdout","text":"Parsing ../input/lakh-midi-clean/10cc/Im_Not_In_Love.3.mid\nParsing ../input/lakh-midi-clean/10cc/Dreadlock_Holiday.3.mid\nParsing ../input/lakh-midi-clean/10cc/Im_Not_In_Love.mid\nParsing ../input/lakh-midi-clean/10cc/Dreadlock_Holiday.1.mid\nParsing ../input/lakh-midi-clean/10cc/Im_Not_In_Love.1.mid\nParsing ../input/lakh-midi-clean/10cc/Dreadlock_Holiday.2.mid\nParsing ../input/lakh-midi-clean/10cc/The_Things_We_Do_for_Love.mid\nParsing ../input/lakh-midi-clean/10cc/Im_Not_In_Love.2.mid\nParsing ../input/lakh-midi-clean/10cc/Dreadlock_Holiday.mid\nParsing ../input/lakh-midi-clean/10cc/Dreadlock_Holiday.4.mid\n","output_type":"stream"},{"name":"stderr","text":"/opt/conda/lib/python3.10/site-packages/keras/src/layers/rnn/rnn.py:204: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.\n  super().__init__(**kwargs)\n","output_type":"stream"},{"name":"stdout","text":"Epoch 1/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m15s\u001b[0m 271ms/step - loss: 4.8948\nEpoch 2/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 278ms/step - loss: 4.1659\nEpoch 3/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m8s\u001b[0m 269ms/step - loss: 4.0405\nEpoch 4/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m10s\u001b[0m 270ms/step - loss: 3.9536\nEpoch 5/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 279ms/step - loss: 3.8464\nEpoch 6/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m8s\u001b[0m 272ms/step - loss: 3.7524\nEpoch 7/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m8s\u001b[0m 267ms/step - loss: 3.7861\nEpoch 8/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 275ms/step - loss: 3.6712\nEpoch 9/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 286ms/step - loss: 3.6290\nEpoch 10/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 275ms/step - loss: 3.5437\nEpoch 11/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 275ms/step - loss: 3.4506\nEpoch 12/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 278ms/step - loss: 3.3544\nEpoch 13/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 284ms/step - loss: 3.3445\nEpoch 14/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 278ms/step - loss: 3.1392\nEpoch 15/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 278ms/step - loss: 3.1881\nEpoch 16/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 286ms/step - loss: 3.0528\nEpoch 17/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 285ms/step - loss: 2.9391\nEpoch 18/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 284ms/step - loss: 2.8851\nEpoch 19/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 284ms/step - loss: 2.7905\nEpoch 20/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 289ms/step - loss: 2.7154\nEpoch 21/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 283ms/step - loss: 2.5922\nEpoch 22/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 280ms/step - loss: 2.5315\nEpoch 23/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 277ms/step - loss: 2.4869\nEpoch 24/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 285ms/step - loss: 2.4046\nEpoch 25/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 278ms/step - loss: 2.3313\nEpoch 26/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 278ms/step - loss: 2.2465\nEpoch 27/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 286ms/step - loss: 2.1343\nEpoch 28/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 278ms/step - loss: 2.1192\nEpoch 29/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 277ms/step - loss: 1.9973\nEpoch 30/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m8s\u001b[0m 268ms/step - loss: 2.1670\nEpoch 31/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 279ms/step - loss: 2.8396\nEpoch 32/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 274ms/step - loss: 2.6935\nEpoch 33/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m8s\u001b[0m 273ms/step - loss: 2.3678\nEpoch 34/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 277ms/step - loss: 1.8769\nEpoch 35/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 291ms/step - loss: 1.7581\nEpoch 36/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 277ms/step - loss: 1.8041\nEpoch 37/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 280ms/step - loss: 1.6912\nEpoch 38/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 282ms/step - loss: 1.6102\nEpoch 39/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 282ms/step - loss: 1.5512\nEpoch 40/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 277ms/step - loss: 1.4932\nEpoch 41/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 279ms/step - loss: 1.5458\nEpoch 42/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 289ms/step - loss: 1.4418\nEpoch 43/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 280ms/step - loss: 1.3157\nEpoch 44/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 278ms/step - loss: 1.4344\nEpoch 45/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 278ms/step - loss: 1.2903\nEpoch 46/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 287ms/step - loss: 1.1836\nEpoch 47/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 274ms/step - loss: 1.1689\nEpoch 48/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 279ms/step - loss: 1.0986\nEpoch 49/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 279ms/step - loss: 1.1025\nEpoch 50/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 285ms/step - loss: 1.0525\nEpoch 51/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 280ms/step - loss: 1.0346\nEpoch 52/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 280ms/step - loss: 1.0186\nEpoch 53/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 281ms/step - loss: 0.9383\nEpoch 54/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 279ms/step - loss: 0.9355\nEpoch 55/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 278ms/step - loss: 0.9431\nEpoch 56/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 282ms/step - loss: 0.9277\nEpoch 57/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 290ms/step - loss: 0.8720\nEpoch 58/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 280ms/step - loss: 0.8286\nEpoch 59/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 279ms/step - loss: 0.7946\nEpoch 60/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 280ms/step - loss: 0.7224\nEpoch 61/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 285ms/step - loss: 0.7746\nEpoch 62/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 275ms/step - loss: 0.7410\nEpoch 63/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 276ms/step - loss: 0.6846\nEpoch 64/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 290ms/step - loss: 0.6615\nEpoch 65/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 283ms/step - loss: 0.6841\nEpoch 66/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 282ms/step - loss: 0.6366\nEpoch 67/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 277ms/step - loss: 0.6295\nEpoch 68/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 286ms/step - loss: 0.6003\nEpoch 69/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 278ms/step - loss: 0.5724\nEpoch 70/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 276ms/step - loss: 0.5453\nEpoch 71/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 280ms/step - loss: 0.5305\nEpoch 72/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 283ms/step - loss: 0.5344\nEpoch 73/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 276ms/step - loss: 0.5257\nEpoch 74/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 281ms/step - loss: 0.4767\nEpoch 75/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 290ms/step - loss: 0.4497\nEpoch 76/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 279ms/step - loss: 0.4485\nEpoch 77/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 281ms/step - loss: 0.4394\nEpoch 78/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 283ms/step - loss: 0.4547\nEpoch 79/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 295ms/step - loss: 0.4100\nEpoch 80/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 284ms/step - loss: 0.3969\nEpoch 81/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 287ms/step - loss: 0.3860\nEpoch 82/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 281ms/step - loss: 0.4990\nEpoch 83/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 298ms/step - loss: 0.3684\nEpoch 84/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 281ms/step - loss: 0.3332\nEpoch 85/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 285ms/step - loss: 0.3077\nEpoch 86/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 286ms/step - loss: 0.3570\nEpoch 87/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 290ms/step - loss: 0.3173\nEpoch 88/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 282ms/step - loss: 0.2891\nEpoch 89/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 288ms/step - loss: 0.2867\nEpoch 90/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 288ms/step - loss: 0.2845\nEpoch 91/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 284ms/step - loss: 0.2631\nEpoch 92/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 284ms/step - loss: 0.2551\nEpoch 93/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 290ms/step - loss: 0.2628\nEpoch 94/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 283ms/step - loss: 0.2688\nEpoch 95/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 285ms/step - loss: 0.2727\nEpoch 96/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 287ms/step - loss: 0.2252\nEpoch 97/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 293ms/step - loss: 0.2405\nEpoch 98/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 284ms/step - loss: 0.2303\nEpoch 99/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 288ms/step - loss: 0.2277\nEpoch 100/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 287ms/step - loss: 0.1850\nEpoch 101/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 293ms/step - loss: 0.1859\nEpoch 102/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 281ms/step - loss: 0.2458\nEpoch 103/200\n\u001b[1m31/31\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 283ms/step - loss: 0.1740\nEpoch 104/200\n\u001b[1m20/31\u001b[0m \u001b[32m━━━━━━━━━━━━\u001b[0m\u001b[37m━━━━━━━━\u001b[0m \u001b[1m3s\u001b[0m 278ms/step - loss: 0.1763","output_type":"stream"}]},{"cell_type":"code","source":"def generate():\n    with open('./notes', 'rb') as filepath:\n        notes = pickle.load(filepath)\n\n \n    name_of_pitch = sorted(set(item for item in notes))\n    n_vocab = len(set(notes))\n\n    , normalized_input = prepare_sequences(notes, name_of_pitch, n_vocab)\n    model = create_network(normalized_input, n_vocab)\n    prediction_output = generate_notes(model, inputs_model, name_of_pitch, n_vocab)\n    create_midi(prediction_output)","metadata":{},"execution_count":null,"outputs":[]},{"cell_type":"code","source":"import numpy as np\n\ndef prepare_sequences(notes, n_vocab, max_sequence_length=100, data_augmentation=True):\n    note_to_int = dict((note, number) for number, note in enumerate(n_vocab))\n\n    sequences = []\n    for i in range(0, len(notes) - max_sequence_length, 1):\n        sequence = notes[i:i + max_sequence_length]\n        sequences.append([note_to_int[char] for char in sequence])\n\n    # data augmentation just to increase diversity /and/or flex audio processing skillz \n    if data_augmentation:\n        augmented_sequences = []\n        for sequence in sequences:\n            # random cropping coz why not\n            start_index = np.random.randint(0, len(sequence) - max_sequence_length)\n            cropped_sequence = sequence[start_index:start_index + max_sequence_length]\n            augmented_sequences.append(cropped_sequence)\n\n            # enabling time shifting to give more variety\n            shift_amount = np.random.randint(-5, 6)  #just a random value that i got off of some dude on internet\n            shifted_sequence = np.roll(sequence, shift_amount)\n            augmented_sequences.append(shifted_sequence)\n\n            # shifting pitch again more variety (why would any sane person do this i dont know.)\n            pitch_shift = np.random.randint(-2, 3)\n            shifted_sequence = [note + pitch_shift for note in sequence]\n            shifted_sequence = [max(0, note) for note in shifted_sequence]  # still ensure they stay in some range, dont have random notes all over the place\n            augmented_sequences.append(shifted_sequence)\n\n        sequences.extend(augmented_sequences)\n\n    # fill up the sequences to max length, to provide regularity in the data\n    padded_sequences = np.array(sequences, dtype=np.int32)\n    padded_sequences = np.pad(padded_sequences, ((0, 0), (0, max_sequence_length - padded_sequences.shape[1])), mode='constant')\n\n    # inp outp sequences, simple python\n    inputs_model = padded_sequences[:, :-1]\n    output_model = padded_sequences[:, -1]\n\n    # ahah now uve messed everything up so try to \n    inputs_model = inputs_model / float(n_vocab)\n\n    return inputs_model, output_model","metadata":{},"execution_count":null,"outputs":[]},{"cell_type":"code","source":"def create_network(inputs_model, n_vocab):\n    model = Sequential()\n    model.add(LSTM(\n        512,\n        input_shape=(inputs_model.shape[1], inputs_model.shape[2]),\n        recurrent_dropout=0.3,\n        return_sequences=True\n    ))\n    model.add(LSTM(512, return_sequences=True, recurrent_dropout=0.3,))\n    model.add(LSTM(512))\n    model.add(BatchNorm())\n    model.add(Dropout(0.3))\n    model.add(Dense(256))\n    model.add(Activation('relu'))\n    model.add(BatchNorm())\n    model.add(Dropout(0.3))\n    model.add(Dense(n_vocab))\n    model.add(Activation('softmax'))\n    model.compile(loss='categorical_crossentropy', optimizer='rmsprop')\n# Load the weights to each node\n    model.load_weights('./weights-improvement-199-0.0327-bigger.hdf5')\n\n    return model","metadata":{},"execution_count":null,"outputs":[]},{"cell_type":"code","source":"def generate_notes(model, inputs_model, name_of_pitch, n_vocab):\n\n    start = numpy.random.randint(0, len(inputs_model)-1)\n\n    int_to_note = dict((number, note) for number, note in enumerate(name_of_pitch))\n\n    pattern = inputs_model[start]\n    prediction_output = []\n\n    # generate 500 notes\n    for note_index in range(500):\n        prediction_input = numpy.reshape(pattern, (1, len(pattern), 1))\n        prediction_input = prediction_input / float(n_vocab)\n\n        prediction = model.predict(prediction_input, verbose=0)\n\n        index = numpy.argmax(prediction)\n        result = int_to_note[index]\n        prediction_output.append(result)\n        pattern.append(index)\n        pattern = pattern[1:len(pattern)]\n\n    return prediction_output\n        ","metadata":{},"execution_count":null,"outputs":[]},{"cell_type":"code","source":"def create_midi(prediction_output):\n    offset = 0\n    output_notes = []\n\n    # create note and chord objects based on the values generated by the model\n    for pattern in prediction_output:\n        # pattern is a chord\n        if ('.' in pattern) or pattern.isdigit():\n            notes_in_chord = pattern.split('.')\n            notes = []\n            for current_note in notes_in_chord:\n                new_note = note.Note(int(current_note))\n                new_note.storedInstrument = instrument.Piano()\n                notes.append(new_note)\n            new_chord = chord.Chord(notes)\n            new_chord.offset = offset\n            output_notes.append(new_chord)\n        # pattern is a note\n        else:\n            new_note = note.Note(pattern)\n            new_note.offset = offset\n            new_note.storedInstrument = instrument.Piano()\n            output_notes.append(new_note)\n\n        # increase offset each iteration so that notes do not stack\n        offset += 0.5\n\n    midi_stream = stream.Stream(output_notes)\n\n    midi_stream.write('midi', fp='test_output.mid')","metadata":{},"execution_count":null,"outputs":[]},{"cell_type":"code","source":"from music21 import instrument, note, stream, chord\ngenerate()\n#to get an output lol :>","metadata":{},"execution_count":null,"outputs":[]}]}