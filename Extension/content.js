// chrome.runtime.sendMessage({todo:"showActionPage"});

window.addEventListener("load", (e) => {
  chrome.storage.sync.set({ status: 0 });
});

var url;

async function getData() {
  // const res=await fetch(urlOfJson)
  // if(res.json()){
  //   chrome.runtime.sendMessage({todo:"msg9",message:"NOT Error"});
  // }else{
  //   chrome.runtime.sendMessage({todo:"msg9",message:"Error"});
  // }
  // return (await fetch(urlOfJson)).json();

  const location = window.location.hostname;

  try {
    const fetchResponse = await fetch("https://456915cc4cc8.ngrok.io/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        url: url,
      }),
    });
    if (fetchResponse.ok) {
      chrome.runtime.sendMessage({ todo: "msg9", message: "NOT Error" });
      return fetchResponse.json();
    } else {
      chrome.runtime.sendMessage({ todo: "msg9", message: "Error" });
    }
  } catch (e) {
    chrome.runtime.sendMessage({ todo: "msg9", message: JSON.stringify(e) });
  }
}

chrome.runtime.onMessage.addListener(async (req, sender, sendRes) => {
  if (req.todo == "hideComments") {
    url = req.message;

    chrome.runtime.sendMessage({ todo: "msg1" });
    var hidden = [];
    var data = await getData();
    data.forEach((element) => {
      if (element.value == 0) {
        hidden.push(element.index);
      }
    });

    chrome.runtime.sendMessage({ todo: "msg4", message: hidden });
    var msg;
    var x = [];
    var imgSrc = [];
    var msgs = [];
    var j = 0;
    var p = 0;
    $("#contents")
      .children()
      .each((i) => {
        msg = $("#content-text").text();
        // msg=msg.replace(/\s+/g, '');
        msgs[j] = msg;
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
        chrome.runtime.sendMessage({ todo: "msg9", message: msgs[i] });
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
