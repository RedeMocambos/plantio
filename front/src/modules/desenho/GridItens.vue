<template>
    <v-container
        fluid
        grid-list-xl
    >
        <v-layout
            row
            wrap
        >
            <v-flex
                xs12
            >
                <v-card
                    <v-card-title
                    class="subheading">
                    Selecione:
                    </v-card-title>
                    <v-layout>
                        <div
                            v-for="(linha, pos_x) of localGridData"
                        >
                            <div
                                v-for="(valor, pos_y) of linha"
                                :style="{width: opt.boxSizeW + 'px', height:opt.boxSizeH + 'px'}"
                            >
                                <div
                                    :style="{width: opt.boxSizeW + 'px', height:opt.boxSizeH + 'px'}"
                                    :class="pontoSelecionado(valor)"
                                    style="border: 1px solid #ccc; padding: 6px "
                                    @mousedown="dragStart()"
                                    @mousemove="trocaValor(pos_x, pos_y)"
                                    @mouseup="dragEnd()"/>
                            </div>
                        </div>
                    </v-layout>
                </v-card>
            </v-flex>
            <v-flex
                xs12
            >
                <v-card>
                    <v-textarea
                        :value="saidaJson"
                        label="Saída json"
                        class="caption"
                    >
                        {{ saidaJson }}
                    </v-textarea>
                </v-card>
            </v-flex>
        </v-layout>
    </v-container>
</template>
<script>
export default {
    name: 'GridItens',
    props: {
        gridData: {
            type: Array,
            default: () => {},
        },
        colorScale: {
            type: Object,
            default: () => {},
        },
        opt: {
            type: Object,
            default: () => {},
        },
    },
    data() {
        return {
            output: '',
            localGridData: [],
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
            posX,
            posY,
        ) {
            if (!this.dragging) {
                return;
            }
            const valor = this.localGridData[posX][posY].value;

            const newRow = this.localGridData[posX].slice(0);

            if (valor < 10) {
                newRow[posY].value = parseInt(valor) + 1;
            } else {
                newRow[posY].value = 0;
            }

            this.$set(this.localGridData, posX, newRow);
        },
        pontoSelecionado(valor) {
            if (typeof valor.value !== 'undefined') {
                return this.colorScale[valor.value];
            }
        },
    },
};
</script>
