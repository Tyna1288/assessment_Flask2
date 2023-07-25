
function snakeToCamel(str) {
  return str.replace(/_(\w)/g, (match, p1) => p1.toUpperCase());
}


