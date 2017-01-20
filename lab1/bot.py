from sopel import module
from emo.wdemotions import EmotionDetector

emo = EmotionDetector()
sumVector = [0.0,0.0,0.0,0.0,0.0,0.0]
count = 0

@module.rule('')
def hi(bot, trigger):
    global sumVector, count
    print(trigger, trigger.nick)
    emoVector = emo.detect_emotion_in_raw_np(trigger)
    avVector = []
    count += 1
    for i in range(len(emoVector)):
        sumVector[i] += emoVector[i]
        avVector.append(sumVector[i]/count)
    print('anger: '+str(avVector[0])+' disgust: '+str(avVector[1])+' fear: '+str(avVector[2])+' joy: '+str(avVector[3])+'sadness: '+str(avVector[4])+'surprise: '+str(avVector[5]))
    #bot.say('Hi, ' + trigger.nick)


