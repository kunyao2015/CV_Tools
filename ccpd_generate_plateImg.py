provinces = ["Íî", "»¦", "½ò", "Óå", "¼½", "½ú", "ÃÉ", "ÁÉ", "¼ª", "ºÚ", "ËÕ", "Õã", "¾©", "Ãö", "¸Ó", "Â³", "Ô¥", "¶õ", "Ïæ", "ÔÁ", "¹ð", "Çí", "´¨", "¹ó", "ÔÆ", "²Ø", "ÉÂ", "¸Ê", "Çà", "Äþ", "ÐÂ", "¾¯", "Ñ§", "O"]
alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
             'X', 'Y', 'Z', 'O']
ads = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
       'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'O']
	
def parse(pic_name):
    iname = pic_name.rsplit('.',1)[0].split('-')
	[leftup, rightdown] = [[int(eel) for eel in el.split('&')] for el in iname[2].split('_')]
	label = iname[-3].split('_')
	real = provinces[int(label[0])] + alphabets[int(label[1])]
	for i in range(2,7):
	    real += ads[int(label[i])]
	return real, [leftup, rightdown]
	
	
# ´´½¨³µÅÆÑµÁ·Êý¾Ý¼¯²âÊÔ¼¯ÎÄ¼þ¼Ð
def mk_dirs(train_dir = '', test_dir = ''):
    if not os.path.exists(train_dir):
	    os.makedirs(train_dir)
	if not os.path.exists(test_dir):
	    os.makedirs(test_dir)
		
#ÌáÈ¡³µÅÆÍ¼Æ¬
def convert_plate_imgs():
    file_path = '....../ccpd_datasets'
	lp = os.listdir(file_path)
	i = 0
	j = 0
	for l in lp:
		if os.path.isdir(file_path+l) and l != 'ccpd_np' and l != 'plate':
			for pic in glob.glob(file_path+l+'/*.jpg'):
		        try:
				    i += 1
					img = cv2.imread(pic)
					real, loc = parse(pic)
					leftUp = loc[0]
					rightDown = loc[1]
					corpImg = img[leftUp[1]:rightDown[1],leftUp[0]:rightDown[0]]
					cv2.imwrite(file_path+'plate'+real+.'.jpg', corpImg, [int(cv2.IMWRITE_JPEG_QUALITY),100])
				except:
				    print(pic + 'is wrong')
				
		    print("%s dir converted done!" % l)
	print("ALL converted done! %d plates are saved!" % i)
	
def split_test_files():
    lp_dir = ''
	test_dir = ''
	lp = os.listdir(lp_dir)
	random.shuffle(lp)
	i = 0
	for l in lp:
	    rate =random.random()
		if rate > 0.9:
		    i += 1
			shutil.move(lp_dir+l, test_dir+l)
			
	print("%d iamges move to test dir" % i)
	
	
if __name__ == 'main':
    mk_dirs()
	convert_plate_imgs()
	split_test_files()
		
					