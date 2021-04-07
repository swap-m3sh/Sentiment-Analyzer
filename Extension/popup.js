var checkBox=document.getElementById('filterCB');

chrome.storage.sync.get(['status'],(res)=>{
    console.log(res.status);
    if(res.status==1){

        checkBox.checked=true;
       
    }
});

checkBox.addEventListener('change',function(){
    // location.reload();

    if(this.checked ){
        checked();
    }

    else{
        chrome.storage.sync.set({'status':0})
        chrome.tabs.query({active: true, currentWindow: true}, (tabs) => {
            let url = tabs[0].url;
            console.log(`${url}`);

            chrome.tabs.sendMessage(tabs[0].id,{todo:'UnHideComments'});
            console.log('unhide message sent');
        });
    }
});

function checked(){
    chrome.storage.sync.set({'status':1})
           
    chrome.tabs.query({active: true, currentWindow: true}, (tabs) => {
        let url = tabs[0].url;
        console.log(`${url}`);

        chrome.tabs.sendMessage(tabs[0].id,{todo:'hideComments'});
        console.log('message sent');

        var notify={
            type:'basic',
            iconUrl:'Logos/youtubeLogo128.png',
            title:'Filtering Started',
            message:'Filtering process is started. Please do not close or reload this tab'
        };
        chrome.notifications.create('notification', notify,()=>{
            console.log('Notified');
        });

    });
}


// var btn=document.getElementById('filterBtn');
// btn.addEventListener('click',function(){
    
//         chrome.tabs.query({active: true, currentWindow: true}, (tabs) => {
//             let url = tabs[0].url;
//             console.log(`${url}`);

//             chrome.tabs.sendMessage(tabs[0].id,{todo:'hideComments'});
//             console.log('message sent');
//         });
    

    
// });


