// chrome.runtime.onMessage.addListener((request,sender,sendResponse)=>{
//     if(request.todo=="showPageAction"){
//         chrome.tabs.query({active:true, currentWindow:true},(tabs)=>{
//             chrome.pageAction.show(tabs[0].id);
        
//         });
//     }
// });
var count=0;
chrome.runtime.onMessage.addListener((request,sender,sendResponse)=>{
    if(request.todo=="count"){
        count++;
        console.log(count);
        
    }

    if(request.todo=="msg5"){
        console.log(`Prenpend started`);
        
    }

    if(request.todo=="msg9"){
        console.log(`${request.message}`);
        
    }

    if(request.todo=="msg8"){
        console.log(`${request.message} + array`);
        
    }

    if(request.todo=="msg6"){
        console.log(`${request.message}`);
        
    }

    if(request.todo=="msg7"){
        console.log(`${request.message}`);
        
    }

    if(request.todo=="msg4"){
        console.log(`${request.message}`);
        
    }
    if(request.todo=="img"){
        console.log(`${request.image}`);
        
    }

    if(request.todo=="msg1"){
        
        console.log('hide msg recieved');
    }

    if(request.todo=="msg2"){
        console.log('UnHide msg recieved');
    }



    
});