// chrome.runtime.sendMessage({todo:"showActionPage"});

window.addEventListener('load',(e)=>{
  chrome.storage.sync.set({'status':0})
})

chrome.runtime.onMessage.addListener((req, sender, sendRes) => {
  if (req.todo == "hideComments") {
    // const allImg = document.querySelectorAll('.yt-img-shadow');

    // chrome.runtime.sendMessage({todo:"msg8",message:JSON.stringify(allImg, null, 4)});

    chrome.runtime.sendMessage({ todo: "msg1" });
    var msg;
    var x = [];
    var imgSrc = [];

    $("#contents")
      .children()
      .each((i) => {
        msg = $("#content-text").text();
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
      if (i == 2) {
        // chrome.runtime.sendMessage({todo:"msg9",message:x[i]});
        continue;
      } else {
        $("#contents").prepend(x[i]);
      }
    }
    // }, 3000);
  }

  if (req.todo == "UnHideComments") {
    chrome.runtime.sendMessage({ todo: "msg2" });
    for (var i = x.length - 1; i >= 0; i--) {
      if (i == 2) {
        $("#contents").prepend(x[i]);
      }
    }
  }
});
