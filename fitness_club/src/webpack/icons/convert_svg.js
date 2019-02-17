var path = require('path');
const webfontsGenerator = require('webfonts-generator');
const src = path.resolve(__dirname, 'svg');
var fs = require('fs');
var filesList = [];

fs.readdirSync(src).forEach(file => {
  filesList.push(path.resolve(src, file));
})

if(filesList.length > 0) {
  webfontsGenerator({
    files: filesList,
    dest: path.resolve(__dirname, 'dist'),
    types: ['woff']
  }, function(error) {
    if(error) {
      console.log('\x1b[41m\x1b[30m', 'Fail during icons convertion!', error, '\x1b[0m');
    } else {
      console.log('\x1b[42m\x1b[30m', 'All icons converted into fonts!','\x1b[0m');
    }
  })
}
else {
  console.log('\x1b[30m\x1b[44m', 'No svg files found for converting into fonts', '\x1b[0m');
}
