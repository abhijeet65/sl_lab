window.onload = () => {
  const details = [
    {
      name: 'Fortis',
      location:"Bangalore"
    }
    
  ];

  details.forEach((item, index) => {
    
	document.getElementById('h_name').innerHTML = details[index].name;
      document.getElementById('h_loc').innerHTML = details[index].location;
      
    
  });
}
