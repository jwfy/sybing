!function(){
    var aud = $(".aud").get(0);
    aud.pos = 0;
	aud.lrc ="";
    aud.volume = 0.2 //  音量的大小
    LRC = "http://bcs.duapp.com/personmusic/仰望.lrc"
    var flag = 1; //  表示歌词面板是否显示的   1 表示 不显示歌词 0 表示 显示歌词
    var playsum = parseInt($(".list-group li").size());
    var playstyle = 1;   //  播放的方式 1 表示 顺序播放 2 表示随即播放 3 表示单曲循环
	//var no-picurl ="/static/img/no_picture.png";
	var  lrcData;
	//console.log("1"+typeof(lrcData))
    var	 oriTop=219; //  存储着歌词相关的相关数据
    //   对音量的初始化
    function initvolume() {
        var End = $(".music_volume_bar").width();
        var distance = End * aud.volume;
        $("#volume_length").css('width', distance);
        $(".music_volume_control").css('left', distance - 8);
    }
    //  调用上面的函数
    initvolume();

    //   播放音频
    $(".icon-play").bind('click',function(e) {
        e.preventDefault();
        if (aud.pos < 1) {
            $(".icon-forward").trigger('click');
        } else {
            aud.play();
        }
        $(".icon-play").addClass('hidden');
        $(".icon-pause").removeClass('hidden');
        $("#list-" + aud.pos).addClass('music_item_active')
    })

    //  暂停
    $(".icon-pause").bind('click',function(e) {
        e.preventDefault();
        aud.pause();
        $(".icon-play").removeClass('hidden');
        $(".icon-pause").addClass('hidden');
    })

    //  下一首
    $(".icon-forward").bind('click',function(e) {
        e.preventDefault();
        aud.pause();
       
        $(".icon-play").addClass('hidden');
        $(".icon-pause").removeClass('hidden');
        $("#list-" + aud.pos).removeClass('music_item_active')
		var temp = parseInt(aud.pos + 1);
		if (temp > playsum)
			aud.pos = 1
		else
			aud.pos = temp;		
        $('#list-' + aud.pos).addClass('music_item_active');
        aud.setAttribute('src', $("#list-" + aud.pos).find('.music_item_url').html())
		aud.lrc = $("#list-" + aud.pos).find('.music_item_lrcurl').html()
		var picurl = $("#list-" + aud.pos).find('.music_item_picture').html()
		if(picurl !="")   //  没有头像资源
		{
		//console.log("1有头像")
			$(".music_picture").attr('src', picurl)
		}
		else
		{
		//console.log("1暂无头像资源")
			$(".music_picture").attr('src', "/static/img/no_picture.png")
		}
		$(".lrc-panel").css("margin-top","219px").html("正在加载歌词中...");
		if(flag==0){
		//   表示 现在正是 歌词面板 显示
			oriTop=219;
			
			lrcData = showLrc(aud.lrc);
		}
        $(".music_info_title").html($("#list-" + aud.pos).find('.music_item_name').html() + "-" + $("#list-" + aud.pos).find('.music_item_author').html()) ;
        aud.play();
    })

    //  上一首
    $(".icon-backward").bind('click',function(e) {
        e.preventDefault();
        aud.pause();
        var temp = parseInt(aud.pos - 1);
        $(".icon-play").addClass('hidden');
        $(".icon-pause").removeClass('hidden');
        $("#list-" + aud.pos).removeClass('music_item_active')
        if (temp <= 0)
            aud.pos = playsum;
        else
            aud.pos = temp;
        $('#list-' + aud.pos).addClass('music_item_active');
        aud.setAttribute('src', $("#list-" + aud.pos).find('.music_item_url').html());
		$(".lrc-panel").css("margin-top","219px").html("正在加载歌词中...");
		aud.lrc = $("#list-" + aud.pos).find('.music_item_lrcurl').html();
		var picurl = $("#list-" + aud.pos).find('.music_item_picture').html()
		if(picurl !="")   //  没有头像资源
		{
			//console.log("2有头像")
			$(".music_picture").attr('src', picurl)
		}
		else
		{
			//console.log("2暂无头像资源")
			$(".music_picture").attr('src', "/static/img/no_picture.png")
		}
		if(flag==0){
		//   表示 现在正是 歌词面板 显示
			oriTop=219;
			
			lrcData = showLrc(aud.lrc);
		}		
        $(".music_info_title").html($("#list-" + aud.pos).find('.music_item_name').html() + "-" + $("#list-" + aud.pos).find('.music_item_author').html()) ;
        aud.play();
    })

    //  列表中的单击事件
    $(".list-group >li").each(function(index) {
        $(this).bind('click',function(){
            $("#list-" + aud.pos).removeClass('music_item_active');
            aud.pos = $(this).index() - 1;
			if( playstyle ==3)
			   console.log("这是通过end的事件，激发的这个操作")
            $(".icon-forward").trigger('click');
        })
    })

    //   音量的控制
    $(".music_volume_bar,#volume_length").bind('click',function(e) {
        var volume = $(".music_volume_bar").offset();
        var Start = volume.left;
        var End = $(".music_volume_bar").width();

        var currentVloume = e.clientX - Start;
        aud.volume = parseFloat(currentVloume / End);

        $("#volume_length").css('width', currentVloume);
        $(".music_volume_control").css('left', currentVloume - 8);

        if (aud.volume > 0.6) $(".music_volume_tool_main span").removeClass('icon-volume-low').removeClass('icon-volume-mute2').addClass('icon-volume-medium');
        else $(".music_volume_tool_main span").removeClass('icon-volume-medium').removeClass('icon-volume-mute2').addClass('icon-volume-low');
    })

    //  音量中的那个大的 控制（暂时还没有弄出滑动）
    $(".music_volume_tool_main span").bind('click',function(e) {
        $(".music_volume_tool_main span").removeClass('icon-volume-low').removeClass('icon-volume-medium').addClass('icon-volume-mute2');
        $(".music_volume_control").css('left', -8);
        $("#volume_length").css('width', 0);
        aud.volume = 0;
    })

    $(".music_load_bar,#music_lenght").bind('click',function(e) {
        var Start = $(".music_load_bar").offset().left;
        var End = $(".music_load_bar").width();

        var currentRun = e.clientX - Start;
        var distance = currentRun / End * aud.duration;
        aud.currentTime = distance;
        $("#music_lenght").css('width', currentRun);
        $(".music_load_control").css('left', currentRun - 8);
    })

    $(".music_picture").bind('click',function(e) {
        if (flag == 1) {
            $(".music").css('display', 'none');
            $(".music_lrc").css('display', 'block');
			if(aud.lrc!=""){
				lrcData = {}
				//oriTop=219;
				lrcData = showLrc(aud.lrc);
				}
			else
				$(".lrc-panel").html("暂无歌词！！！")
			//console.log("2"+typeof(lrcData))
            flag = 0;
        } else {
            $(".music").css('display', 'block');
            $(".music_lrc").css('display', 'none');
            flag = 1;
        }
    })

    function showLrc(url) {
	    //console.log("这次的歌曲是"+url);
		oriTop = 219
        var xmlhttp,words = {}, times = [];
		var musicData = {ti:'',ar:'',al:''};
        //   加载lrc 歌词文件
        loadLrc(url);
        function loadLrc(url) {
            if (url == "") {
                alert("暂无歌词");
            } else {
                xmlhttp = null;
                if (window.XMLHttpRequest) {
                    xmlhttp = new XMLHttpRequest();
                } else if (window.ActiveXObject) {
                    xmlhttp = new ActiveXObject('Microsoft.XMLHTTP');
                }
                if (xmlhttp != null) {
                    xmlhttp.onreadystatechange = getXMLHttpData;
                    xmlhttp.open('get', url, true);
                    xmlhttp.send(null);
                } else {
                    alert("您的浏览器不支持XMLHTTP，暂时不能播放歌词");
                }
            }
        }
        function getXMLHttpData() {
            if (xmlhttp.readyState === 4) {//  表示以及传送文件完成
            if (xmlhttp.status === 0 || xmlhttp.status === 200) {
				var arr = xmlhttp.responseText.split(/[\r\n]/), 
				  len = arr.length, 
				  i = 0;
				for (; i < len;i++) {
					var temp,doit = true,
						str = decodeURIComponent(arr[i]), 
						word = str.replace(/\[\d*:\d*((\.|\:)\d*)*\]/g, "");
					
					'ti ar al'.replace(/\S+/g,function(a){
						
						if(doit && musicData[a]===""){
							temp = str.match(new RegExp('\\['+a+'\\:(.*?)\\]'));
							if(temp && temp[1]){
								doit = false;
								musicData[a] = temp[1]; 
							}
						}
					});
					var temptime = []
				//	console.log(str);
					temptime = str.match(/\[(\d*):(\d*)([\.|\:]\d*)*\]/g);
					if(temptime == null)  continue;
				//	console.log(temptime);
					var lentime = temptime.length
				//	console.log(lentime);
				//	console.log(typeof(lentime))
					for(var j=0;j<lentime;j++){
						temptime[j].replace(/\[(\d*):(\d*)([\.|\:]\d*)*\]/g, function() {
							var min = arguments[1] | 0, 
								sec = arguments[2] | 0, 
								time = min * 60 + sec,
								p = times.push(time * 1e3);
							words[times[--p]] = word.trim();
							//console.log("时间"+time +"内容"+word.trim())
						});						
					}
				}
				times.sort(function(a, b) {
					return a - b;
				});
				str =""
				for(i=0;i<times.length;i++){
					var t = times[i],w = words[t];
					str += '<p data-lrctime="'+t+'" data-lrctop="'+oriTop+'">'+w+'</p>';
					//console.log("时间"+t +"内容"+w+"高度"+oriTop)
					oriTop-=27;
				}	
				$(".lrc-panel").html(str);
			}
		}
	} 
	return {
			words: words,
			times: times,
			data:musicData
		};	
	}

    function moveLrc(currenttime) {
	    var words = {}, times = [];
        words = lrcData.words;
		times = lrcData.times;
		var  len = times.length, i = 0,
          curTime = currenttime*1e3|0;
		//console.log("现在的时间是"+currenttime+"现在的高度是 "+ $(".lrc-panel").css("margin-top"));
        for(;i<len;i++){
            var t = times[i]; 
              
            if (curTime > t && curTime < times[i + 1]) {
				var $cur = $(".lrc-panel").find('[data-lrctime="'+t+'"]');
                var top = $cur.attr('data-lrctop');
				
				
				$(".lrc-panel").stop().animate({marginTop:top}).find('p.lrc-current').removeClass('lrc-current');
				$cur.addClass('lrc-current')
                break;
            }
        }
		
    }

    //  对时间进行处理
    function TimeDeal(time) {
        var minute = parseInt(time / 60);
        var second = parseInt(time % 60);
        minute = minute >= 10 ? minute: "0" + minute;
        second = second >= 10 ? second: "0" + second;
        return minute + ":" + second;
    }

    aud.addEventListener('progress',function(e) {
        var width = parseFloat($(".music_load_bar").css('width'));
        var precwidth = parseFloat(e.loaded / e.total) * width;
        $("#music_load").css('width', precwidth);
    },
    false)

    aud.addEventListener('timeupdate',function(eve) {
        var width = parseFloat($(".music_load_bar").css('width'));
        var precwidth = parseFloat(aud.currentTime / aud.duration) * width ;
        $("#music_lenght").css('width', precwidth);
        if ($(".music_load_control").css('left') >= width - 30) $(".music_load_control").css('right', -30)
        else $(".music_load_control").css('left', precwidth - 8);
        setInterval(function() {
            var CurrentTime = TimeDeal(aud.currentTime);
            var AllTime = TimeDeal(aud.duration);
            $(".music_info_time").html(CurrentTime + "|" + AllTime);
        },
        1000);
		moveLrc(aud.currentTime);
    },
    false);

    aud.addEventListener('canplay',function(evt) {
        $('#jukebox .play').trigger('click');
    });

    aud.addEventListener('ended',function(eve) {
		var pos =0 
		if(playstyle ==2)   //  随机播放的
		{
		 //   console.log("共有几首歌曲?"+playsum)
			var pos = parseInt(Math.random()*playsum+1) ;
		//	console.log("现在是随即播放,而且是第"+pos);
		}else if(playstyle==3)   //  单曲循环
		{
			pos = aud.pos;
			//console.log("现在是单曲循环,而且是第"+pos);
		}
		if(pos !=0)
		{
			$("#list-"+pos).trigger('click')
			//console.log("现在不是顺序播放的，模拟单击事件"+pos);
			//console.log("现在的播放方式是"+playstyle);
		}
		else
		{
			$(".icon-forward").trigger('click');
		}
		//   这里就是判断是哪种播放方式的
        
		$(".lrc-panel").css("margin-top","219px");
		//oriTop=219;
    },
    false);
	
	
	
	//  显示 播放 条件的 菜单栏
    var show = 1
	$("#playstyle").click(function(){
	    if(show == 1)
		{
		$(".music_show_playstyle").css("display","block");
		show = 0;
		}
	})
	
	
	
	//  播放方式的 选择
	$("#icon-list").click(function(){
		$("#playstyle").removeClass().addClass("icon-list").attr("title","顺序播放")
		$(".music_show_playstyle").css("display","none");
		show = 1;
		playstyle =1 ;   //  播放方式
	})

	$("#icon-loop").click(function(){
		$("#playstyle").removeClass().addClass("icon-loop").attr("title","单曲循环")
		$(".music_show_playstyle").css("display","none");
		show = 1;
		playstyle =3 ;   //  播放方式
	})
	
	$("#icon-shuffle").click(function(){
		$("#playstyle").removeClass().addClass("icon-shuffle").attr("title","随机播放")
		$(".music_show_playstyle").css("display","none");
		show = 1;
		playstyle =2 ;   //  播放方式
	})
	

}();