# Windows
# Selenium

__version__ = '0.1.0'
__description__ = 'Automation for downloading of wells'

# Import modules
import os
import time
from selenium import webdriver
from datetime import datetime

def main():
	cwd = os.getcwd()
	# Start timing
	startTime = time.time()

	print "[" + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "]: Opening Chrome"
	driver = webdriver.Chrome("/Library/Python/2.7/site-packages/selenium/webdriver/chrome/chromedriver")
	homepage = 'http://122.54.214.222/databank/ProvSum.asp'
	driver.get(homepage)


	# Get all the homepage_links
	province_links = driver.find_elements_by_tag_name('a')

	# Dictionary
	url_dict_province = getURLs(province_links,'provwells', 'openlayers')
	url_dict_muni = {}
	for name_province, url_province in sorted(url_dict_province.iteritems()):
		driver.get(url_province)
		muni_links = driver.find_elements_by_tag_name('a')
		print "[" + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "]: Getting the municipalities urls --- " + name_province
		url_dict_muni.update(getURLs(muni_links,'MunWells', 'MunWells'))
		driver.get(homepage)
		province_path = os.path.join(cwd,name_province)
		if not os.path.exists(province_path):
			os.makedirs(province_path)

	for name_muni, url_muni in sorted(url_dict_muni.iteritems()):
		print "[" + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "]: Looping through the municipalities' urls --- " + name_muni
		driver.get(url_muni)
		pages_links = driver.find_elements_by_tag_name('a')
		list_page_url = []

		print "[" + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "]: Getting the number of pages"
		for pages_link in pages_links:
			page_url = pages_link.get_attribute('href')
			if '&pg=' in page_url:	
				list_page_url.append(page_url)

		for page in list_page_url:
			driver.get(page)
			pageSource = driver.page_source
			page_num = page.split('&pg=')[1]
			province_dir = page.split('&province=')[1].split('&mun=')[0].replace('%20',' ')
			print "[" + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "]: Saving xls file --- " + province_dir, name_muni, page_num

			with open(province_dir + '/' + name_muni +' Ground Water Data ' + page_num + '.xls', "w") as xls_file:
				xls_file.write(pageSource.encode('"iso-8859-15"'))
				print "[" + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "]: File saved! " + name_muni +' Ground Water Data ' + page_num + '.xls'
			xls_file.close()

	driver.close()
	endTime = time.time()  # End timing
	print '\nElapsed Time:', str("{0:.2f}".format(round(endTime - startTime,2))), 'seconds'

# Loop through the list of province links
def getURLs (links, key1, key2):
	url_dict = {}
	for link in links:
		url =  link.get_attribute('href')

		# Filter urls: province name
		if key1 in url or key2 in url:
			pass
		else:
			# To avoid duplicates urls
			if url in url_dict.values():
				pass
			else:
				area_name = link.text
				url_dict[area_name] = url
	return url_dict

if __name__ == "__main__":
    main()