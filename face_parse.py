import os, sys, select, subprocess


if __name__ == "__main__":
    args = ['sh', '-c', './interactive_face_detection_demo -i cam -m /opt/intel/computer_vision_sdk/deployment_tools/intel_models/face-detection-adas-0001/FP32/face-detection-adas-0001.xml -m_ag /opt/intel/computer_vision_sdk/deployment_tools/intel_models/age-gender-recognition-retail-0013/FP32/age-gender-recognition-retail-0013.xml -r']

    p1 = subprocess.Popen(args, stdout=subprocess.PIPE)

    age, gender, emotion = "", "", ""

    while True:
        # Read and parse from intel's thing
        rlist, wlist, xlist = select.select([p1.stdout], [], [])
        for stdout in rlist:
            parser = os.read(stdout.fileno(), 1024)
            if len(parser) > 0:
                if 'age' in parser:
                    split_parser = parser.split('= ')[1].split(',')
                    gender = split_parser[0]
                    age = split_parser[1].rstrip()
                elif 'emotion' in parser:
                    emotion = parser.split('= ')[1]

            # print to output once all fields filled
            if len(age) > 0 and len(gender) > 0 and len(emotion) > 0:
                string_to_print = ""
                if len(sys.argv) > 0:
                    if 'age' in str(sys.argv):
                        string_to_print += age
                    if 'gender' in str(sys.argv):
                        if len(string_to_print) > 0:
                            string_to_print += ' '
                        string_to_print += gender
                    if 'emotion' in str(sys.argv):
                        if len(string_to_print) > 0:
                            string_to_print += ' '
                        string_to_print += emotion
                    if len(string_to_print) > 0:
                        print(string_to_print)

                age, gender, emotion = "", "" ,""
