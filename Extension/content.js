// chrome.runtime.sendMessage({todo:"showActionPage"});

window.addEventListener('load',(e)=>{
  chrome.storage.sync.set({'status':0})
})

// var url;

async function getData(){
  
  let url='http://127.0.0.1:5500/Extension/comment.json';
    return (await fetch(url)).json();
   
    
  // $.post('/submitJSONData',  // url
  //      { myData: url }, // data to be submit
  //      function(data, status, xhr) {   // success callback function
  //       for(var i=0;i<3;i++){
  //         if(data.i==1){
  //           arr.push(i);
  //         }
  //       }
  //           },
  //      'json');
}


chrome.runtime.onMessage.addListener(async(req, sender, sendRes) => {
  if (req.todo == "hideComments") {
    
    // arr=getData();
    // url=req.message;
      
    chrome.runtime.sendMessage({ todo: "msg1" });
    var hidden=[];
    var data=await getData();
    data.forEach((element)=>{
      if(element.value==0){
        hidden.push(element.Index);
      }
    })
   
    chrome.runtime.sendMessage({todo:"msg4",message:hidden});
    var msg;
    var x = [];
    var imgSrc = [];
    var msgs=[];
    var j=0;
    var p=0;
    $("#contents")
      .children()
      .each((i) => {
        msg = $("#content-text").text();
        // msg=msg.replace(/\s+/g, ''); 
        msgs[j]=msg;
        j++;
        imgSrc[i] = $("#img").attr("src");
        // imgSrc[i]=$('#content-text').text();

        x[i] = $("#comment").parent().detach();

        // chrome.runtime.sendMessage({todo:"count",count:i});
        // chrome.runtime.sendMessage({todo:"msg4",message:msg});
      });
    // var j=0;
    // setTimeout(()=>{
    for (var i = x.length - 1; i >= 0; i--) {
      // chrome.runtime.sendMessage({todo:"msg5",message:msg});
      // chrome.runtime.sendMessage({todo:"msg6",message:imgSrc[j]});
      // j++;
      // if(imgSrc[i]=='https://yt3.ggpht.com/ytc/AAUvwnjEt2U7ffjo_Lx4NcBRYVU3E9ocPD6UpHQ0Ow=s88-c-k-c0x00ffffff-no-rj'){
      //     chrome.runtime.sendMessage({todo:"msg7",message:true});
      // }
      if (hidden.includes(i)) {
        chrome.runtime.sendMessage({todo:"msg9",message:msgs[i]});
        continue;
      } else {
        p++;
        $("#contents").prepend(x[i]);
      }
      
      // if(hidden.includes(msgs[i])){
      //   chrome.runtime.sendMessage({ todo: "msg6",message:hidden[p] });
      //   // p--;
      //   continue;
      // }else{
      //   $("#contents").prepend(x[i]);
      // }
    }
    // }, 3000);
    
    
  }

  if (req.todo == "UnHideComments") {
    chrome.runtime.sendMessage({ todo: "msg2" });
    location.reload();
  }
});



