<template>
    <div>
        <h3 class="card-title">Selecione:</h3>
        <div
            v-for="(linha, pos_x) of localGridData"
            class="row"
            style="margin-bottom:0; margin-left:30px">
            <div
                v-for="(valor, pos_y) of linha"
                :style="{width: opt.boxSizeW + 'px', height:opt.boxSizeH + 'px'}"
                class="col"
                style="margin:0; padding:0">
                <div
                    :style="{width: opt.boxSizeW + 'px', height:opt.boxSizeH + 'px'}"
                    :class="pontoSelecionado(valor)"
                    style="border: 1px solid #ccc; padding: 6px "
                    @mousedown="dragStart()"
                    @mousemove="trocaValor(pos_x, pos_y)"
                    @mouseup="dragEnd()"/>
            </div>
        </div>

        <h3 class="card-title">Saida json:</h3>
        <textarea rows="3">{{ saidaJson }}</textarea>
    </div>
</template>
<script>
export default {
    name: 'GridItens',
    props: {
        gridData: null,
        scale: null,
        opt: null,
    },
    data() {
        return {
            output: '',
            localGridData: [
                [] = ';',
            ],
            dragging: false,
        };
    },
    computed: {
        saidaJson() {
            return JSON.stringify(this.localGridData);
        },
    },
    watch: {
        gridData() {
            this.localGridData = this.gridData;
        },
    },
    created() {
        this.localGridData = this.gridData;
    },
    methods: {
        dragStart() {
            this.dragging = true;
        },
        dragEnd() {
            this.dragging = false;
        },
        trocaValor(
            pos_x,
            pos_y,
        ) {
            if (!this.dragging) {
                return;
            }
            const valor = this.localGridData[pos_x][pos_y].value;

            const newRow = this.localGridData[pos_x].slice(0);

            if (valor < 10) {
                newRow[pos_y].value = parseInt(valor) + 1;
            } else {
                newRow[pos_y].value = 0;
            }

            this.$set(this.localGridData, pos_x, newRow);
        },
        pontoSelecionado(valor) {
            return this.scale[valor.value];
        },
    },
};
</script>
