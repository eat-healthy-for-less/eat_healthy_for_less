
all:
	for i in `find . -name "*.md"`; do j=$${i%%.md}; markdown_py -e utf8 $${j}.md > $${j}.html; done

clean:
	for i in `find . -name "*.md"`; do j=$${i%%.md}; rm -f $${j}.html; done


rsync:
	rsync -avz . trey0.org:/var/www-eathealthyforless.org/
