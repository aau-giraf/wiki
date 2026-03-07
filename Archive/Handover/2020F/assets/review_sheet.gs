function getPullInfo(repository,id, _) {
  var url = 'https://api.github.com/repos/aau-giraf/' + repository + '/pulls/' + id;
  // GENERATE TOKEN ON THE AAUGiraf user from https://github.com/settings/tokens
  var token = "";
  
  var headers = {
    "Authorization" : "Basic " + Utilities.base64Encode("AAUGiraf" + ':' + token)
  };

  var params = {
    "method":"GET",
    "headers":headers
  };
    
  
  var response = UrlFetchApp.fetch(url, params);
  var obj = JSON.parse(response);
  Logger.log(obj.state);
  
  var string = ""
  
  string += obj.created_at + ";";
  string += obj.additions + ";";
  string += obj.deletions + ";";
  string += obj.html_url + ";";
  string += obj.state + ";";
  string += obj.draft;
  
  return string;
}

function updateInfo() {
  var range = SpreadsheetApp.getActiveSpreadsheet().getSheets()[1].getRange("A2");
    
  var value = range.getValue();
  
  value = (value + 1) % 10;
  
  range.setValue(value);
}

function getAllOpenPRs(repository, _) {
  var url = 'https://api.github.com/repos/aau-giraf/' + repository + '/pulls?state=open';
  var response = UrlFetchApp.fetch(url);
  var obj = JSON.parse(response);
  
  var openPRs = "";
  
  for (i = 0; i < obj.length; i++){
    openPRs += obj[i].number + ";";
  }
  
  return openPRs;
  
}

