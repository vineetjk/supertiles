import os

result = []

delete_these = ['trigd2.png','arrows.png','trigu2.png','progress.gif','mast2.png','loading.gif','logo.png','map4.jpg','botmen2.png']

def find_files(filename, search_path):
   

# Wlaking top-down from the root
   for root, dir, files in os.walk(search_path):
      if filename in files:
         result.append(os.path.join(root, filename))
   return result

for i in delete_these:
    print(find_files(i,"/home/vins/Downloads/tilestilespics/"))


for item in result:
    print(item)
    os.remove(item)