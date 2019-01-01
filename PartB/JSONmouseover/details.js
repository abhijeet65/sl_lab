window.onload = () => {
  const details = [
    {
      model: 'Baleno',
      name: 'Suzuki',
      price: '7 lakhs',
      year: '20/09/16',
    },
    {
      model: 'i20',
      name: 'Hyundai',
      price: '9 lakhs',
      year: '05/07/15',
    },
    {
      model: 'Accord',
      name: 'Honda',
      price: '25 lakhs',
      year: '27/03/13',
    },
    {
      model: 'C220d',
      name: 'Mercedes-Benz',
      price: '45 lakhs',
      year: '04/11/17',
    },
  ];

  details.forEach((item, index) => {
    const listElement = document.createElement('th');
    listElement.onmouseover = () => {
      document.getElementById('name').innerHTML = details[index].name;
      document.getElementById('model').innerHTML = details[index].model;
      document.getElementById('price').innerHTML = details[index].price;
      document.getElementById('year').innerHTML = details[index].year;
    };
    listElement.innerHTML = item.name;
    document.getElementById('menu').appendChild(listElement);
  });
}
