const exec = require('child_process').execSync;
const fs = require('fs');
const slugify = require('@sindresorhus/slugify');

var name = 'practicalai'
const list = require('./'+name+'.json');
exec(`mkdir -p mp3/${name}/`)
function run(list) {
  list.forEach(function(item) {
    var title = getTitle(item);
    console.log(title);
    const cmd = `wget -O mp3/${name}/${title} -q ${item.link}`
    exec(cmd, {encoding: 'utf8'});
  });
}

function getTitle(item) {
  var a = slugify(item.title);
  var arr = item.url.split('/');
  var b = arr[arr.length-1]
  var no = a.split('-')[0];
  return b + '_' + a + '.mp3';
}

run(list);
