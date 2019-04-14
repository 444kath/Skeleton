import os, sys, select, subprocess


if __name__ == "__main__":
    args = ['sh', '-c', '/home/intel/inference_engine_samples/intel64/Release/interactive_face_detection_demo -i cam -m /opt/intel/computer_vision_sdk/deployment_tools/intel_models/face-detection-adas-0001/FP32/face-detection-adas-0001.xml -m_ag /opt/intel/computer_vision_sdk/deployment_tools/intel_models/age-gender-recognition-retail-0013/FP32/age-gender-recognition-retail-0013.xml -m_em /opt/intel/computer_vision_sdk/deployment_tools/intel_models/emotions-recognition-retail-0003/FP32/emotions-recognition-retail-0003.xml -r']

    p1 = subprocess.Popen(args, stdout=subprocess.PIPE)

    age, gender, emotion = "", "", ""

    for i in range(20):
        age, gender, emotion = "", "", ""
    	while len(emotion) == 0 and len(age) == 0 and len(gender) == 0:
            # Read and parse from intel's thing
            rlist, wlist, xlist = select.select([p1.stdout], [], [])
            for stdout in rlist:
               parser = os.read(stdout.fileno(), 1024)
               if len(parser) > 0:
                   if 'age' in parser:
                       split_parser = parser.split('= ')
  		       if len(split_parser) > 1:
                           new_parser = split_parser[1]
                           new_parser = new_parser.split(',')
                           gender = new_parser[0]
                           age = new_parser[1].split('\n')[0]
	                   if len(split_parser) > 2:
			       emotion = split_parser[2].split('\n')[0]
                   elif 'emotion' in parser:
                       if len(split_parser) > 1:
                           emotion = parser.split('= ')[1]

    # print to output once all fields filled
    if 'M' in gender:
        print(age + ' year old male.  He looks ' + emotion)
    else:
        print(age + ' year old female.  She looks ' + emotion)

