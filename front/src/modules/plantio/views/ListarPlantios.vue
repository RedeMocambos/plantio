<template>
    <v-container fluid>
        <v-layout>
            <v-flex
                xs10
                offset-xs1
            >
                <v-data-table
                    :headers="header"
                    :items="plantios"
                >
                    <template
                        v-slot:items="props"
                    >
                        <td>{{ props.index + 1 }}</td>
                        <td>
                            {{ props.item.especie }}
                        </td>
                        <td>
                            {{ props.item.area }}
                        </td>
                        <td>
                            {{ props.item.data_plantio }}
                        </td>
                        <td>
                            {{ props.item.dimensao }} {{ props.item.unidade_medida }}
                        </td>
                        <td>
                            {{ props.item.espacamento }}
                        </td>
                        <td>
                            {{ props.item.densidade }}
                        </td>
                        <td>
                            {{ props.item.estado }}
                        </td>
                        <td>
                            <v-btn
                                flat
                                small
                                @click="visualizar(props.item.id)"
                            >
                                <v-icon class="pr-2">
                                    grid_on
                                </v-icon>
                                ver
                            </v-btn>
                            <v-btn
                                flat
                                small
                                @click="editar(props.item.id)"
                            >
                                <v-icon class="pr-2">
                                    edit
                                </v-icon>
                                editar
                            </v-btn>
                            <v-btn
                                flat
                                small
                                @click="excluir(props.item.id)"
                            >
                                <v-icon class="pr-2">
                                    clear
                                </v-icon>
                                excluir
                            </v-btn>
                        </td>
                    </template>
                </v-data-table>
                <v-btn
                    dark
                    class="green darken-1"
                    @click="adicionar()"
                >
                    <v-icon
                        white
                        class="pr-2">
                        add
                    </v-icon>
                    adicionar plantio
                </v-btn>
            </v-flex>
        </v-layout>
    </v-container>
</template>
<script>
import { mapActions, mapGetters } from 'vuex';

export default {
    name: 'ListarPlantios',
    data() {
        return {
            header: [
                {
                    text: '#',
                    align: 'center',
                    sortable: false,
                    value: 'numero',
                },
                {
                    align: 'center',
                    text: 'espécie',
                    value: 'especie',
                },
                {
                    align: 'center',
                    text: 'área',
                    value: 'area',
                },
                {
                    align: 'center',
                    text: 'data de plantio',
                    value: ' data_plantio',
                },
                {
                    align: 'center',
                    text: 'dimensão',
                    value: 'dimensao',
                },
                {
                    align: 'center',
                    text: 'espaçamento',
                    value: 'espacamento',
                },
                {
                    align: 'center',
                    text: 'densidade',
                    value: 'densidade',
                },
                {
                    align: 'center',
                    text: 'estado',
                    value: 'estado',
                },
                {
                    align: 'center',
                    text: 'ações',
                    value: 'acoes',
                },
            ],
            plantios: [],
        };
    },
    computed: {
        ...mapGetters({
            listaPlantios: 'plantio/plantios',
        }),
    },
    watch: {
        listaPlantios() {
            this.plantios = this.listaPlantios;
        },
    },
    created() {
        this.buscarPlantios();
    },
    methods: {
        ...mapActions({
            buscarPlantios: 'plantio/buscarPlantios',
            adicionarPlantio: 'plantio/adicionarPlantio',
        }),
        visualizar(id) {
            const path = `/plantio/${id}`;
            this.$router.push({ path });
        },
        editar(id) {
            const path = `/plantio/${id}/edit`;
            this.$router.push({ path });
        },
        adicionar() {
            this.adicionarPlantio({
                especie: '',
                area: '',
                data_plantio: '',
                dimensao: '',
                unidade_medida: '',
                espacamento: '',
                densidade: '',
                estado: '',
            }).then((response) => {
                this.editar(response.id);
            });

        },
        excluir(id) {
        },
    },
};
</script>
