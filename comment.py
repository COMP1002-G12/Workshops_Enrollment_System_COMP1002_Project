dictionary=dict()
average=dict()
l=[]
def determine_number(x):
    if x==5:
        return '5'
    elif x==4:
        return '4'
    elif x==3:
        return '3'
    elif x==2:
        return '2'
    elif x==1:
        return '1'
    else:
        return '0'
def main():
    sum=0
    choose=input("which workshop do you choose:")
    mark=eval(input('which grade will you give to our workshop:'))
    while True:
        if mark not in range(0,6):
            mark=eval(input('please remark'))
        else:
            grades=determine_number(mark)
            break
    if choose not in dictionary.keys():        
        dictionary[choose]={'0':0,'1':0,'2':0,'3':0,'4':0,'5':0}
        if grades in dictionary[choose].keys():
            dictionary[choose][grades]+=1
    else:
        if grades in dictionary[choose].keys():
            dictionary[choose][grades]+=1
    for k,v in dictionary[choose].items():
        sum=v+sum
    averag=(0*dictionary[choose]['0']+1*dictionary[choose]['1']+2*dictionary[choose]['2']+3*dictionary[choose]['3']+4*dictionary[choose]['4']+5*dictionary[choose]['5'])/sum
    average[choose]=averag
    print('{0:^18}'.format('workshop'),'|','{0:^18}'.format('average'),sep='')
    print('-'*36)
    for k,v in average.items():
        print('{0:^18}'.format(k),'|','{0:^18}'.format(round(v,2)),sep='')
    return average
