function long()
{
        var vals = document.getElementById('input1').value.split(' ');
        var maxi = vals[0];
        vals.forEach(function(v){
			if(v.length>maxi.length)
				maxi = v;
			});
        document.getElementById('sp1').textContent = maxi + '   length:   ' + maxi.length;
}
