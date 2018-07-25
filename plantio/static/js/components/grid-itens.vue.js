Vue.component('grid-itens', {
    template:
    `
<div>
  <h3 class="card-title">Selecione:</h3>  
  <div v-for="(linha, pos_x) of localGridData" class="row" style="margin-bottom:0; margin-left:30px">
    <div v-for="(valor, pos_y) of linha" class="col" style="width:24px; height:24px; margin:0; padding:0;" >
      <div v-on:click="trocaValor(pos_x, pos_y)" style="border: 1px solid #ccc; width:24px; height:24px; padding:6px"  :class="pontoSelecionado(valor)">
      </div>
    </div>
  </div>
  
  <h3 class="card-title">Saida json:</h3>
  <span>{{saidaJson}}</span>
</div>
`,
    props: {
	gridData: null
    },
    data: function() {
	return {
	    output: '',
	    localGridData: [
		[] = ';'
	    ]
	}
    },
    created: function() {
	this.localGridData = this.gridData;
    },
    methods: {
	trocaValor: function(pos_x, pos_y) {
	    let valor = this.localGridData[pos_x][pos_y];
	    const newRow = this.localGridData[pos_x].slice(0)
	    newRow[pos_y] = (valor == '1') ? '0' : '1';
	    this.$set(this.localGridData, pos_x, newRow);
	},
	pontoSelecionado: function(valor) {
	    if (valor === '1') {
		return "teal darken";
	    } else {
		return "grey lighten-5";
	    }
	}
    },
    computed: {
	saidaJson: function() {
	    return JSON.stringify(this.localGridData);
	}
    },
});
