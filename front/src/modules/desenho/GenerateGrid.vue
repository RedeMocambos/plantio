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
                <v-btn
                    @click="parseGrid()"
                    class="green lighten-1"
                >
                    <v-icon
                        class="pr-2"
                    >
                        format_paint
                    </v-icon>
                    gerar desenho
                </v-btn>
            </v-flex>
            <v-flex>
                <GridItens
                    :opt="opt"
                    :color-scale="colorScale"
                    :grid-data="localData"/>
            </v-flex>
        </v-layout>
    </v-container>
</template>
<script>
import { mapActions } from 'vuex';
import GridItens from './GridItens';

export default {
    name: '',
    components: {
        GridItens,
    },
    props: {
        colorScale: {
            type: Object,
            default: () => {},
        },
        dimensions: {
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
            localData: [
                [] = '0',
            ],
            localOpt: {},
        };
    },
    mounted() {
        this.localOpt = this.opt;
    },
    methods: {
        ...mapActions({
            defineGridData: 'desenho/defineGridData',
        }),
        parseGrid() {
            this.localData = this.generateGrid();
        },
        generateGrid() {
            if (typeof this.dimensions.sizeX === 'undefined'
                || typeof this.dimensions.sizeY === 'undefined'
            ) {
                return;
            }
            const grid = [];
            let xIn = 0;
            let yIn = 0;
            const scaleLength = Object.keys(this.colorScale).length - 2;
            const maxColorByDensity = Math.round((scaleLength * this.localOpt.density) / this.localOpt.densityMax);
            for (let x = 0; x < this.dimensions.sizeX; x += 1) {
                xIn = (Math.round(this.dimensions.sizeX / 2) * -1) + x + 1;
                grid[x] = [];
                for (let y = 0; y < this.dimensions.sizeY; y += 1) {
                    yIn = (Math.round(this.dimensions.sizeY / 2) * -1) + y + 1;
                    const color = 0;
                    if (color > maxColorByDensity) {
                        color = maxColorByDensity;
                    }
                    grid[x][y] = {
                        x: xIn,
                        y: yIn,
                        value: color,
                    };
                }
            }
            return grid;
        },
    },
    watch: {
        dimensions() {
            if (this.dimensions.sizeX !== null &&
                this.dimensions.sizeY !== null
            ) {
                this.parseGrid();
            }
        },
    },
};
</script>
